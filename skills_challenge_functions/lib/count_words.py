'''
A function called count_words that takes a string as an argument and
returns the number of words in that string.
'''
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    return word_count


