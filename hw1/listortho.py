"""
CMSC 14200: list-based spell-checker and tab-completer Distribution

Adam Shaw
Winter 2023

YOUR NAME HERE
"""


class ListOrthographer:
    """
    Class for a list-based orthographer
    """

    def __init__(self):
        '''
        Constructor

        Parameters:
          none

        Initialize empty list of words.
        '''
        self.words = []

    def insert(self, word):
        '''
        Insert the word into the orthographer if it consists only of lowercase
        letters and is not already present.

        Parameters:
          word : str

        Returns: (does not return a value)
        '''
        raise NotImplementedError("todo: ListOrthographer.insert")

    def insert_from_file(self, filename):
        '''
        Read the named file, insert words (one per line in file).

        Parameters:
          filename : str

        Returns: (does not return a value)
        '''
        raise NotImplementedError("todo: ListOrthographer.insert_from_file")

    def contains(self, word):
        '''
        Check presence of given word in the orthographer.

        Parameters:
          word : str

        Returns: boolean
        '''
        raise NotImplementedError("todo: ListOrthographer.contains")

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        raise NotImplementedError("todo: ListOrthographer.completions")

    def num_completions(self, prefix):
        '''
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        raise NotImplementedError("todo: ListOrthographer.num_completions")

    def all_words(self):
        '''
        Return all the words in the orthographer. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        raise NotImplementedError("todo: ListOrthographer.all_words")

    def num_words(self):
        '''
        Return the number of words in the orthographer.

        Parameters:
          none

        Returns: int
        '''
        raise NotImplementedError("todo: ListOrthographer.num_words")
