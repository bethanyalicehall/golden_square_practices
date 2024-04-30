from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
When we add two diary entries
it appears in the list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    entry_2 = DiaryEntry("Tuesday", "I am hungry today")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
When we add two diary entries
and call #count_words, the sum
of all the words in the 
contents of the entries will be
returned
"""
def test_count_words_returns_count_of_all_words():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    entry_2 = DiaryEntry("Tuesday", "I am hungry today")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 8

"""
When we add two diary entries
with a total length of 8 and I call 
#reading_time with a wpm of 2 the total
reading time should be 4 minutes
"""
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    entry_2 = DiaryEntry("Tuesday", "I am hungry today")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 4

"""
When we add a diary entry
I call #find_best_entry_for_reading_time
with a wpm and minutes that allows me to read it
that entry is returned
"""
def test_find_best_entry_for_reading_time_returns_none():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_1

"""
When we add a diary entry
I call #find_best_entry_for_reading_time
with a wpm and minutes that means I cannot read it
None is returned
"""
def test_find_best_entry_for_reading_time_returns_entry_that_is_readable():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 1) == None

"""
When we add two diary entries
one long and one short, and
I call #find_best_entry_for_reading_time
with a wpm and minutes that mean we can only
read the short one, then it returns the shorter one.
"""
def test_find_best_entry_for_reading_time_returns_short():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    entry_2 = DiaryEntry("Tuesday", "Good day")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 1) == entry_2

"""
When we add two diary entries
one longer and one shorter, and
I call #find_best_entry_for_reading_time
with a wpm and minutes it returns the one closest
to the reading time
"""
def test_find_best_entry_for_reading_time_returns_shortest():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "I am tired today")
    entry_2 = DiaryEntry("Tuesday", "Today has been a great day")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_2

