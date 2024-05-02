from unittest.mock import Mock
from lib.track import Track

'''
Matches returns true
when a search keyword matches 
a title
'''

def test_matches_on_full_title():
    track = Track("Meow", "Cat")
    assert track.matches("Meow") == True


'''
Matches returns true
when a search keyword matches 
a partial title
'''

def test_matches_on_partial_title():
    track = Track("Meow", "Cat")
    assert track.matches("Me") == True

'''
Matches returns true
when a search keyword matches 
an artist
'''

def test_matches_on_full_artist():
    track = Track("Meow", "Cat")
    assert track.matches("Cat") == True

'''
Matches returns true
when a search keyword matches 
an artist partially
'''

def test_matches_on_partial_artist():
    track = Track("Meow", "Cat")
    assert track.matches("Ca") == True

'''
Matches returns False
when there is no match in title or
artist
'''

def test_matches_returns_false():
    track = Track("Meow", "Cat")
    assert track.matches("Dog") == False