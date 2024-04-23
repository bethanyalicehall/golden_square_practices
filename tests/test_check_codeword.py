from lib.check_codeword import *

'''
If the code word is correct "horse"
returns "Correct! Come in."
'''
def test_check_codeword_correct():
    codeword = "horse"
    result = check_codeword(codeword)
    assert result == "Correct! Come in."

'''
If the code word is close "house"
returns "Close, but nope."
'''
def test_check_codeword_close():
    codeword = "house"
    result = check_codeword(codeword)
    assert result == "Close, but nope."

'''
If the code word is incorrect "dog"
returns "WRONG!"
'''
def test_check_codeword_incorrect():
    codeword = "dog"
    result = check_codeword(codeword)
    assert result == "WRONG!"