from lib.make_snippet import *

'''
Given a string of four 
words, returns string
'''
def test_return_string_of_less_than_five_words():
    result = make_snippet("Today I ate cake")
    assert result == "Today I ate cake"

'''
Given a string of five 
words, returns string
'''
def test_return_string_of_five_words():
    result = make_snippet("Today I went sofa shopping")
    assert result == "Today I went sofa shopping"


'''
Given a string longer
than five words, returns
string with '...' at end of five words
'''
def test_return_string_longer_than_five_words():
    result = make_snippet("Today I went sofa shopping with my partner")
    assert result == "Today I went sofa shopping..."


