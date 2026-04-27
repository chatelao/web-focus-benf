from antlr4 import InputStream, CommonTokenStream
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser
from antlr4.error.ErrorListener import ErrorListener
import sys

class BailErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")

def check_fex(text):
    input_stream = InputStream(text)
    lexer = WebFocusReportLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(BailErrorListener())
    stream = CommonTokenStream(lexer)
    parser = WebFocusReportParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(BailErrorListener())
    try:
        parser.start()
        return True, ""
    except Exception as e:
        return False, str(e)

samples = {
    "sample4": """JOIN AS_ROOT PRODUCT_CATEGORY AND PRODUCT_SUBCATEG IN WF_RETAIL
  TO UNIQUE PRODUCT_CATEGORY AND PRODUCT_SUBCATEGORY IN PROJECTED
  AS J1
END
TABLE FILE WF_RETAIL
SUM PROJECTED_SALE_UNITS REVENUE_US
BY PRODUCT_CATEGORY
ON TABLE SET PAGE NOPAGE
END
""",
    "sample5": """JOIN FILE VIDEOTRK AT MOVIECODE TAG V1 TO ALL
     FILE MOVIES   AT RELDATE   TAG M1 AS JW1
  WHERE DATEDIF(RELDATE, TRANSDATE,'Y') GT 10;
  WHERE V1.MOVIECODE EQ M1.MOVIECODE;
END
TABLE FILE VIDEOTRK
 SUM TITLE/A25 AS 'Title'
     TRANSDATE AS 'Last,Transaction'
     RELDATE AS 'Release,Date'
 COMPUTE YEARS/I5 = (TRANSDATE - RELDATE)/365; AS 'Years,Difference'
 BY TITLE NOPRINT
 BY HIGHEST 1 TRANSDATE NOPRINT
END
""",
    "sample6": """JOIN INNER CURR_JOBCODE IN EMPINFO TO MULTIPLE JOBCODE IN JOBINFO AS J0
JOIN INNER EMP_ID IN EMPINFO TO MULTIPLE EMP_ID IN EDINFO AS J1
SET MULTIPATH=COMPOUND
TABLE FILE EMPINFO
PRINT LAST_NAME FIRST_NAME COURSE_NAME JOB_DESC
END
"""
}

for name, text in samples.items():
    ok, err = check_fex(text)
    if ok:
        print(f"{name}: OK")
    else:
        print(f"{name}: FAILED - {err}")
