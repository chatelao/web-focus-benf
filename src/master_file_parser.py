from antlr4 import InputStream, CommonTokenStream
from MasterFileLexer import MasterFileLexer
from MasterFileParser import MasterFileParser as GeneratedMasterFileParser
from antlr4.error.ErrorListener import ErrorListener
import sys

class BailErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")

class MasterFileParserWrapper:
    def __init__(self):
        pass

    def parse(self, text):
        input_stream = InputStream(text)
        lexer = MasterFileLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(BailErrorListener())

        stream = CommonTokenStream(lexer)
        parser = GeneratedMasterFileParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(BailErrorListener())

        return parser.start()

class MasterFileParser:
    def __init__(self):
        self.wrapper = MasterFileParserWrapper()

    def parse(self, text):
        return self.wrapper.parse(text)

if __name__ == "__main__":
    sample_mf = """
    FILENAME=EMPLOYEE, SUFFIX=FOC, MFD_PROFILE=baseapp/DDBAEMP,$
    VARIABLE NAME = Emptitle, USAGE=A30, DEFAULT=EMPID,$
    SEGMENT=EMPDATA,SEGTYPE=S0, $
    FIELDNAME=PIN   , ALIAS=ID, USAGE=A9, INDEX=I,   TITLE='&&Emptitle',$
    FIELDNAME=LASTNAME,     LN,       A15,             $
    DEFINE AREA/A13=DECODE DIV (NE 'NORTH EASTERN' SE 'SOUTH EASTERN' CE 'CENTRAL' WE 'WESTERN' CORP 'CORPORATE' ELSE 'INVALID AREA');$
    """
    parser = MasterFileParser()
    try:
        tree = parser.parse(sample_mf)
        print(tree.toStringTree(recog=None))
    except Exception as e:
        print(f"Error parsing Master File:\n{e}")
        sys.exit(1)
