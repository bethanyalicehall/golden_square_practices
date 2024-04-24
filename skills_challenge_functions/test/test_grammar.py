from lib.grammar import *
import pytest

'''
Given a text that is 
capitalized and ends with 
a full stop returns True
'''

def test_check_grammar_capitalized_and_full_stop():
    text = "I am happy."
    question = False
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == True

'''
Given a text that is 
capitalized and ends with 
an exclamation mark returns True
'''

def test_check_grammar_capitalized_and_exclamation():
    text = "I am happy!"
    question = False
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == True

'''
Given a text that is 
capitalized and ends with 
a question mark returns True
'''

def test_check_grammar_capitalized_and_question():
    text = "Am I happy?"
    question = True
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == True


'''
Given a non valid text (no capital
or punctuation) where question = False
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
Given a non valid text (capital
but no punctuation) where question = False
it returns a 
capitalized text with a full stop
at the end.
'''

def test_adds_full_stop():
    text = "I am happy"
    question = False
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "I am happy."

'''
Given a non valid text (punctuation
but no capital) where question = False
it returns a 
capitalized text with a full stop
at the end.
'''

def test_adds_capital():
    text = "i am happy."
    question = False
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "I am happy."

'''
Given a non valid text (no capital
or question mark)
where question = True
it returns a capitalized
text with a question mark at the end.
'''

def test_adds_capital_and_question_mark():
    text = "how are you"
    question = True
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "How are you?"

'''
Given a non valid text (capital
but no question mark)
where question = True
it returns a capitalized
text with a question mark at the end.
'''

def test_adds_question_mark():
    text = "How are you"
    question = True
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "How are you?"

'''
Given a non valid text (question 
mark but no capital)
where question = True
it returns a capitalized
text with a question mark at the end.
'''

def test_adds_capital_to_question():
    text = "how are you?"
    question = True
    result = capitalizes_and_adds_full_stop(text, question)
    assert result == "How are you?"

'''
Given an input of something 
other than a boolean
for the question it returns an
error message
'''

def test_returns_error_if_not_boolean():
    text = "how are you"
    question = None
    with pytest.raises(TypeError, match=r"Question parameter must be a boolean value."):
        capitalizes_and_adds_full_stop(text, question)

'''
Given an input of something 
other than a string
it returns an error message
'''
def test_returns_error_if_not_string():
    text = None
    question = False
    with pytest.raises(Exception, match=r"Invalid input format. Please provide a text string."):
        result = capitalizes_and_adds_full_stop(text, question)