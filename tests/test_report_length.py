from lib.report_length import *

def test_report_length():
    str = "horse"
    length = 5
    result = report_length(str)
    assert result == f"This string was {length} characters long."