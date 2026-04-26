import unittest
from src.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):
    def test_global_definition_and_lookup(self):
        st = SymbolTable()
        st.define("var1", "integer", value=10)

        symbol = st.lookup("var1")
        self.assertIsNotNone(symbol)
        self.assertEqual(symbol.name, "var1")
        self.assertEqual(symbol.symbol_type, "integer")
        self.assertEqual(symbol.metadata['value'], 10)

    def test_case_insensitivity(self):
        st = SymbolTable()
        st.define("MyVar", "string")

        symbol = st.lookup("MYVAR")
        self.assertIsNotNone(symbol)

        symbol2 = st.lookup("myvar")
        self.assertIsNotNone(symbol2)

    def test_nested_scoping(self):
        st = SymbolTable()
        st.define("global_var", "string")

        st.enter_scope()
        st.define("local_var", "integer")

        # Should see both
        self.assertIsNotNone(st.lookup("global_var"))
        self.assertIsNotNone(st.lookup("local_var"))

        st.exit_scope()

        # Should only see global
        self.assertIsNotNone(st.lookup("global_var"))
        self.assertIsNone(st.lookup("local_var"))

    def test_shadowing(self):
        st = SymbolTable()
        st.define("var", "global")

        st.enter_scope()
        st.define("var", "local")

        symbol = st.lookup("var")
        self.assertEqual(symbol.symbol_type, "local")

        st.exit_scope()

        symbol = st.lookup("var")
        self.assertEqual(symbol.symbol_type, "global")

    def test_local_only_lookup(self):
        st = SymbolTable()
        st.define("global_var", "string")

        st.enter_scope()
        st.define("local_var", "integer")

        self.assertIsNone(st.lookup("global_var", local_only=True))
        self.assertIsNotNone(st.lookup("local_var", local_only=True))

    def test_exit_global_error(self):
        st = SymbolTable()
        with self.assertRaises(Exception):
            st.exit_scope()

if __name__ == '__main__':
    unittest.main()
