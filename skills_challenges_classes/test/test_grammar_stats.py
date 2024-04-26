from lib.grammar_stats import *
import pytest

'''
Given a text that is 
capitalized and ends with 
a full stop returns True
'''

def test_check_grammar_capitalized_and_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("I am happy.")
    assert result == True

'''
Given a text that is 
capitalized and ends with 
an exclamation mark returns True
'''

def test_check_grammar_capitalized_and_exclamation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("I am happy!")
    assert result == True

'''
Given a text that is 
capitalized and ends with 
a question mark returns True
'''

def test_check_grammar_capitalized_and_question():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Am I happy?")
    assert result == True

'''
Given a non valid text (no capital
or punctuation) 
it returns False
'''

def test_returns_false_when_no_capital_or_punct():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("am I happy")
    assert result == False

'''
Given a non valid text (capital
but no punctuation) 
it returns False
'''

def test_returns_false_when_no_punct():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Am I happy")
    assert result == False

'''
Given a non valid text (no capital
but punctuation) 
it returns False
'''

def test_returns_false_when_no_capital():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("am I happy?")
    assert result == False

def test_percentage_good_mixed_texts():
        # Test when some texts have passed and some have not
        grammar_stats = GrammarStats()
        grammar_stats.check("I am happy.")  # Passes
        grammar_stats.check("Am I happy")  # Fails
        assert grammar_stats.percentage_good() == 50 

def test_percentage_all_pass_texts():
        # Test when some texts have passed and some have not
        grammar_stats = GrammarStats()
        grammar_stats.check("I am happy.")  # Passes
        grammar_stats.check("Am I happy?")  # Passes
        assert grammar_stats.percentage_good() == 100

def test_percentage_all_fail_texts():
        # Test when some texts have passed and some have not
        grammar_stats = GrammarStats()
        grammar_stats.check("I am happy")  # Passes
        grammar_stats.check("am I happy?")  # Passes
        assert grammar_stats.percentage_good() == 0

def test_percentage_good_no_texts():
        # Test when no texts have been checked
        grammar_stats = GrammarStats()
        assert grammar_stats.percentage_good() == 0