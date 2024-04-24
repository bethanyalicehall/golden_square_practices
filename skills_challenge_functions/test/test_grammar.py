from lib.grammar import *

'''
Given a text where question = False
it returns a 
capitalized text with a full stop
at the end.
'''

def test_capitalizes_and_adds_full_stop():
    text = "i am happy"
    question = False
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "I am happy."
'''
Given a text where question = True
it returns a capitalized
text with a question mark at the end.
'''

def test_calculates_reading_time_of_text():
    text = "how are you"
    question = True
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "How are you?"