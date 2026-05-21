import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db_utils import is_db_available
from runtime_runner import RuntimeRunner
from asg import MasterFile, Segment, Field
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from antlr4 import CommonTokenStream, InputStream
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry
import json

class TestLiveParity(unittest.TestCase):
    """
    Integration tests against a live PostgreSQL database.
    These tests are skipped if no database is available.
    """

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_live_db_connection(self):
        """
        Verify that we can actually connect and execute a simple query on the live DB.
        """
        with RuntimeRunner() as runner:
            with runner.conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_basic_report_parity(self):
        """
        Verify full pipeline (DDL -> Fixtures -> Transpile -> Execute) on a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="LIVE_SALES")
        s1 = Segment(name="LIVE_SALES")
        s1.fields = [
            Field(name="PROD", alias="PROD", usage="A20"),
            Field(name="PRICE", alias="PRICE", usage="D12.2")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"PROD": "Apple", "PRICE": 1.50},
            {"PROD": "Banana", "PRICE": 0.75},
        ]
        fixture_path = "live_test_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile
            fex_code = """
            TABLE FILE LIVE_SALES
            PRINT PROD PRICE
            ON TABLE HOLD AS LIVE_RESULTS
            END
            """
            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "live_parity_proc")

            # 4. Execute on Live DB
            with RuntimeRunner() as runner:
                # Cleanup if table exists (optional, but good for repeatability)
                with runner.conn.cursor() as cursor:
                    cursor.execute('DROP TABLE IF EXISTS "LIVE_SALES" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "LIVE_RESULTS" CASCADE;')

                runner.setup_schema([f1])
                runner.load_fixtures([("LIVE_SALES", fixture_path)])
                runner.run_procedure(sql_procedure, "live_parity_proc")
                results = runner.fetch_table("LIVE_RESULTS")

            # 5. Verify
            self.assertEqual(len(results), 2)
            prods = {r['PROD'].strip() for r in results}
            self.assertIn("Apple", prods)
            self.assertIn("Banana", prods)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_where_total_parity(self):
        """
        Verify WHERE (pre-aggregation) and WHERE TOTAL (post-aggregation) parity on a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="FILTER_DATA")
        s1 = Segment(name="FILTER_DATA")
        s1.fields = [
            Field(name="REGION", alias="REG", usage="A10"),
            Field(name="PRODUCT", alias="PROD", usage="A20"),
            Field(name="SALES", alias="SALES", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"REGION": "East", "PRODUCT": "Apples", "SALES": 100},
            {"REGION": "East", "PRODUCT": "Apples", "SALES": 100},  # SUM=200
            {"REGION": "West", "PRODUCT": "Apples", "SALES": 300},  # Skipped by WHERE
            {"REGION": "East", "PRODUCT": "Oranges", "SALES": 50},  # SUM=50, skipped by WHERE TOTAL
        ]
        fixture_path = "filter_test_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile
            fex_code = """
            TABLE FILE FILTER_DATA
            SUM SALES
            BY PRODUCT
            WHERE REGION EQ 'East'
            WHERE TOTAL SALES GT 150
            ON TABLE HOLD AS FILTER_RESULTS
            END
            """
            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "filter_parity_proc")

            # 4. Execute on Live DB
            with RuntimeRunner() as runner:
                with runner.conn.cursor() as cursor:
                    cursor.execute('DROP TABLE IF EXISTS "FILTER_DATA" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "FILTER_RESULTS" CASCADE;')

                runner.setup_schema([f1])
                runner.load_fixtures([("FILTER_DATA", fixture_path)])
                runner.run_procedure(sql_procedure, "filter_parity_proc")
                results = runner.fetch_table("FILTER_RESULTS")

            # 5. Verify
            # Expected: Only Apples (East) with SUM=200
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['PRODUCT'].strip(), "Apples")
            self.assertEqual(results[0]['SALES'], 200)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_aggregation_parity(self):
        """
        Verify aggregation (SUM) and grouping (BY) parity on a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="SALES_DATA")
        s1 = Segment(name="SALES_DATA")
        s1.fields = [
            Field(name="PRODUCT", alias="PROD_ALIAS", usage="A20"),
            Field(name="AMOUNT", alias="AMT_ALIAS", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"PRODUCT": "Widgets", "AMOUNT": 100},
            {"PRODUCT": "Widgets", "AMOUNT": 200},
            {"PRODUCT": "Gadgets", "AMOUNT": 50},
        ]
        fixture_path = "aggregation_test_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile
            fex_code = """
            TABLE FILE SALES_DATA
            SUM AMOUNT AS 'AMT_ALIAS'
            BY PRODUCT AS 'PROD_ALIAS'
            ON TABLE HOLD AS AGG_RESULTS
            END
            """
            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "agg_parity_proc")

            # 4. Execute on Live DB
            with RuntimeRunner() as runner:
                with runner.conn.cursor() as cursor:
                    cursor.execute('DROP TABLE IF EXISTS "SALES_DATA" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "AGG_RESULTS" CASCADE;')

                runner.setup_schema([f1])
                runner.load_fixtures([("SALES_DATA", fixture_path)])
                runner.run_procedure(sql_procedure, "agg_parity_proc")
                results = runner.fetch_table("AGG_RESULTS")

            # 5. Verify
            self.assertEqual(len(results), 2)

            # Find Gadgets
            gadgets = next(r for r in results if r['PROD_ALIAS'].strip() == 'Gadgets')
            self.assertEqual(gadgets['AMT_ALIAS'], 50)

            # Find Widgets
            widgets = next(r for r in results if r['PROD_ALIAS'].strip() == 'Widgets')
            self.assertEqual(widgets['AMT_ALIAS'], 300)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_join_parity(self):
        """
        Verify multi-table JOIN parity on a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()

        # Primary File
        f1 = MasterFile(name="ORDERS")
        s1 = Segment(name="ORDERS")
        s1.fields = [
            Field(name="ORDER_ID", alias="OID", usage="I8"),
            Field(name="PROD_ID", alias="PID", usage="I8"),
            Field(name="QTY", alias="QTY", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # Joined File
        f2 = MasterFile(name="PRODUCTS")
        s2 = Segment(name="PRODUCTS")
        s2.fields = [
            Field(name="PROD_ID", alias="PID", usage="I8"),
            Field(name="PROD_NAME", alias="PNAME", usage="A20")
        ]
        f2.segments = [s2]
        registry.register_master_file(f2)

        # 2. Prepare Fixtures
        orders_data = [
            {"ORDER_ID": 101, "PROD_ID": 1, "QTY": 5},
            {"ORDER_ID": 102, "PROD_ID": 2, "QTY": 3},
        ]
        products_data = [
            {"PROD_ID": 1, "PROD_NAME": "Widget"},
            {"PROD_ID": 2, "PROD_NAME": "Gadget"},
        ]

        f1_fixture = "orders_fixtures.json"
        f2_fixture = "products_fixtures.json"

        with open(f1_fixture, "w") as f:
            json.dump(orders_data, f)
        with open(f2_fixture, "w") as f:
            json.dump(products_data, f)

        try:
            # 3. Transpile
            fex_code = """
            JOIN PROD_ID IN ORDERS TO PROD_ID IN PRODUCTS AS J1
            TABLE FILE ORDERS
            PRINT ORDER_ID PROD_NAME QTY
            ON TABLE HOLD AS JOIN_RESULTS
            END
            """
            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "join_parity_proc")

            # 4. Execute on Live DB
            with RuntimeRunner() as runner:
                with runner.conn.cursor() as cursor:
                    cursor.execute('DROP TABLE IF EXISTS "ORDERS" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "PRODUCTS" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "JOIN_RESULTS" CASCADE;')

                runner.setup_schema([f1, f2])
                runner.load_fixtures([
                    ("ORDERS", f1_fixture),
                    ("PRODUCTS", f2_fixture)
                ])
                runner.run_procedure(sql_procedure, "join_parity_proc")
                results = runner.fetch_table("JOIN_RESULTS")

            # 5. Verify
            self.assertEqual(len(results), 2)

            # Sort by ORDER_ID for consistent verification
            results.sort(key=lambda x: x['ORDER_ID'])

            self.assertEqual(results[0]['ORDER_ID'], 101)
            self.assertEqual(results[0]['PROD_NAME'].strip(), "Widget")
            self.assertEqual(results[0]['QTY'], 5)

            self.assertEqual(results[1]['ORDER_ID'], 102)
            self.assertEqual(results[1]['PROD_NAME'].strip(), "Gadget")
            self.assertEqual(results[1]['QTY'], 3)

        finally:
            if os.path.exists(f1_fixture):
                os.remove(f1_fixture)
            if os.path.exists(f2_fixture):
                os.remove(f2_fixture)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_calculated_fields_parity(self):
        """
        Verify DEFINE and COMPUTE parity on a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="CALC_DATA")
        s1 = Segment(name="CALC_DATA")
        s1.fields = [
            Field(name="PRODUCT", alias="PROD", usage="A20"),
            Field(name="AMOUNT", alias="AMT", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"PRODUCT": "Widgets", "AMOUNT": 100},
            {"PRODUCT": "Gadgets", "AMOUNT": 200},
        ]
        fixture_path = "calc_test_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile
            fex_code = """
            DEFINE FILE CALC_DATA
            TAX = AMOUNT * 0.1;
            END
            TABLE FILE CALC_DATA
            SUM AMOUNT TAX
            COMPUTE TOTAL = AMOUNT + TAX;
            BY PRODUCT
            ON TABLE HOLD AS CALC_RESULTS
            END
            """
            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "calc_parity_proc")

            # 4. Execute on Live DB
            with RuntimeRunner() as runner:
                with runner.conn.cursor() as cursor:
                    cursor.execute('DROP TABLE IF EXISTS "CALC_DATA" CASCADE;')
                    cursor.execute('DROP TABLE IF EXISTS "CALC_RESULTS" CASCADE;')

                runner.setup_schema([f1])
                runner.load_fixtures([("CALC_DATA", fixture_path)])
                runner.run_procedure(sql_procedure, "calc_parity_proc")
                results = runner.fetch_table("CALC_RESULTS")

            # 5. Verify
            self.assertEqual(len(results), 2)

            # Find Gadgets: AMT=200, TAX=20, TOTAL=220
            gadgets = next(r for r in results if r['PRODUCT'].strip() == 'Gadgets')
            self.assertEqual(float(gadgets['AMOUNT']), 200.0)
            self.assertEqual(float(gadgets['TAX']), 20.0)
            self.assertEqual(float(gadgets['TOTAL']), 220.0)

            # Find Widgets: AMT=100, TAX=10, TOTAL=110
            widgets = next(r for r in results if r['PRODUCT'].strip() == 'Widgets')
            self.assertEqual(float(widgets['AMOUNT']), 100.0)
            self.assertEqual(float(widgets['TAX']), 10.0)
            self.assertEqual(float(widgets['TOTAL']), 110.0)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

if __name__ == '__main__':
    unittest.main()
