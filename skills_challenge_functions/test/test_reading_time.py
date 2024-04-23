from lib.reading_time import *
import pytest

'''
Given a text message with 20 words
It returns 6 seconds
'''
def test_returns_reading_time_of_text_in_seconds():
    text = "Kangaroo " * 20
    result = calculates_reading_time_of_text(text)
    assert result == "6 seconds"

'''
Given a text message with 200 words
It returns 1 minute
'''
def test_returns_reading_time_of_text_in_minutes():
    text = "Pineapple " * 200
    result = calculates_reading_time_of_text(text)
    assert result == "1 minute"

'''
Given a text message with 250 words
It returns 1 minute and 15 seconds
'''
def test_returns_reading_time_of_text_in_minutes_and_seconds():
    text = "Dobby " * 250
    result = calculates_reading_time_of_text(text)
    assert result == "1 minute and 15 seconds"

'''
Given a text message with 0 words
It returns 0 seconds
'''
def test_returns_reading_time_of_text_with_no_words():
    text = "" 
    result = calculates_reading_time_of_text(text)
    assert result == "0 seconds"

'''
Given an input of something 
other than a string
it returns an error message
'''
def test_returns_error_if_not_string():
    text = None
    with pytest.raises(Exception, match=r"Invalid input format. Please provide a text string."):
        result = calculates_reading_time_of_text(text)

