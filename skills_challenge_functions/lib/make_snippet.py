'''
A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
'''

def make_snippet(string):
    words = string.split()  # Split the string into words
    if len(words) <= 5:
        return string
    else:
        snippet_words = ' '.join(words[:5])  # Select the first 5 words
        return f"{snippet_words}..."
    