from lib.music_library import MusicLibrary
from unittest.mock import Mock
'''
When I add multiple tracks
and search for a keyword
i get the matching track back.
'''

def test_searches_for_track_using_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("Thriller") == [fake_matching]