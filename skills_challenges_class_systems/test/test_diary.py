import pytest
from lib.diary import Diary


'''
Initially has an empty
list of entries
'''
def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []


'''
Initially word count
is 0
'''
def test_initially_has_word_count_of_zero():
    diary = Diary()
    assert diary.count_words() == 0

'''
Initially #reading_time should
raise an error
'''
def test_initially_reading_time_should_raise_error():
    diary = Diary()
    with pytest.raises(Exception, match=r"No diary entries added yet"):
        diary.reading_time(2)

'''
Initially #find_best_entry_for_reading_time 
should raise an error
'''
def test_initially_best_entry_should_raise_error():
    diary = Diary()
    with pytest.raises(Exception, match=r"No diary entries added yet"):
        diary.find_best_entry_for_reading_time(2, 2)

