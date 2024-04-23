from lib.count_words import *

'''
A function called count_words that takes a string as an argument and 
returns the number of words in that string.
'''

def test_count_words_in_string():
    result = count_words("I like kangaroos")
    assert result == 3