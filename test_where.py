from antlr4 import *
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser

def test_where():
    cases = [
        "TABLE FILE EMPDATA PRINT SALARY WHERE SALARY GT 1000 AND DEPARTMENT EQ 'SALES' END",
        "TABLE FILE EMPDATA SUM SALARY WHERE TOTAL SALARY EXCEEDS 110000 END",
        "TABLE FILE EMPDATA PRINT * WHERE DEPARTMENT IS 'MIS' OR 'PRODUCTION' END",
        "TABLE FILE EMPDATA PRINT * WHERE LAST_NAME CONTAINS 'JOHN' END",
        "TABLE FILE EMPDATA PRINT * WHERE LAST_NAME LIKE 'BA_N%' END",
        "TABLE FILE EMPDATA PRINT * WHERE SALARY FROM 20000 TO 50000 END",
        "TABLE FILE EMPDATA PRINT * WHERE SALARY NOT-FROM 10000 TO 20000 END",
        "TABLE FILE EMPDATA PRINT * WHERE SALARY IS MISSING END",
        "TABLE FILE EMPDATA PRINT * WHERE PRODUCT_ID IN FILE EXPER END",
        "TABLE FILE EMPDATA PRINT * WHERE SALES IN (43000, 12000, 13000) END",
        "TABLE FILE CAR PRINT COUNTRY WHERE CAR INCLUDES JAGUAR AND JENSEN END",
        "TABLE FILE EMPDATA PRINT * WHERE (LAST_NAME EQ 'CROSS' OR 'JONES') AND (SALARY GT 22000) END",
        "DEFINE FILE EMPDATA RATIO = IF SALARY GT 50000 THEN 1 ELSE 0; END",
    ]
    for text in cases:
        print(f"Parsing: {text}")
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        # print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    try:
        test_where()
    except Exception as e:
        print(e)
