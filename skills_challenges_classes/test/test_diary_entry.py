from lib.diary_entry import *
import pytest

def test_formats_with_title_and_entry():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

def test_count_words_in_diary_entry():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 2

'''
Given an empty contents
or title return an error
'''
def test_error_raised_on_empty_string():
    with pytest.raises(Exception, match=r"Please provide a text string."):
        diary_entry = DiaryEntry("My Title", "")
    with pytest.raises(Exception, match=r"Please provide a text string."):
        diary_entry = DiaryEntry("", "Hello")

'''
Given a wpm of 2 and 3 words
returns a reading time of 2
'''
def test_calculate_reading_time():
    diary_entry = DiaryEntry("My Title", "Some contents and")
    wpm = 2
    result = diary_entry.reading_time(wpm)
    assert result == 2

'''
Given a wpm of 0 
raises an error
'''
def test_raises_error_when_wpm_0():
    diary_entry = DiaryEntry("My Title", "Some content")
    with pytest.raises(Exception, match=r"Please provide an integer of 1 or above."):
        result = diary_entry.reading_time(0)

'''
Given a contents of 6 words
and a wpm of 2 and 1 minute the first
2 words are returned

def test_reading_chunk():
    diary_entry = DiaryEntry("My Title", "One two three four five six")
    wpm = 2
    minutes = 1
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "One two"
    '''