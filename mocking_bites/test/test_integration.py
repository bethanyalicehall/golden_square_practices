from lib.music_library import MusicLibrary
from lib.track import Track
import pytest

'''
When I add multiple tracks they are 
reflected in the track list
'''

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("Thriller", "MJ")
    track_2 = Track("Hey Jude", "The Beatles")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

'''
When I add multiple tracks
and search for a specific title
i get the matching track back.
'''

def test_searches_for_track_using_title():
    library = MusicLibrary()
    track_1 = Track("Thriller", "MJ")
    track_2 = Track("Hey Jude", "The Beatles")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Thriller") == [track_1]