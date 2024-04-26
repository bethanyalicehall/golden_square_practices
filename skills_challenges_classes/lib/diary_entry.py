import math

class DiaryEntry:
    def __init__(self, title, contents):
        if contents == "" or title == "":
            raise Exception("Please provide a text string.")
        self._title = title
        self._contents = contents

    def format(self):
        return f'{self._title}: {self._contents}'

    def count_words(self):
        words = self._contents.split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Please provide an integer of 1 or above.")
        contents_word_count = len(self._contents.split())
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
