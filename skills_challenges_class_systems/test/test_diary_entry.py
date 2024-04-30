from lib.diary_entry import DiaryEntry

"""
When we initialise with a title and 
contents I can get that title and contents back
"""
def test_contstructs_gets_title_and_contents():
    diary_entry = DiaryEntry("Monday", "I am tired today")
    assert diary_entry.title == "Monday"
    assert diary_entry.contents == "I am tired today"

"""
When we initialise with 4 word contents
#count_words should return 4
"""
def test_count_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("Monday", "I am tired today")
    assert diary_entry.count_words() == 4

"""
When we initialise with 5 word contents
then #reading_time with a wpm of 2 should return
3
"""
def test_reading_time_returns_minutes():
    diary_entry = DiaryEntry("Monday", "I am tired today, again.")
    assert diary_entry.reading_time(2) == 3