"""
CMSC 14200: trie-based spell-checker and tab-completer Distribution

Adam Shaw
Winter 2023

YOUR NAME HERE
"""

class Trie:
    """
    Class for representing tries
    """

    def __init__(self, root):
        '''
        Constructor

        Parameters:
         root : str (a character, but Python does not have a "char" type)

        Initialize root to given char, empty dict of children, final to False.
        '''
        self.root = root
        self.children = {}
        self.final = False

    def insert(self, word):
        '''
        Insert the word into the trie.

        Parameters:
	     word : str

        Returns: (does not return a value)
        '''
        raise NotImplementedError("todo: Trie.insert")

    def contains(self, word):
        '''
        Check presence of given word in the trie.

        Parameters:
         word : str

        Returns: boolean
        '''
        raise NotImplementedError("todo: Trie.contains")

    def all_words(self):
        '''
        Return all the words in the trie. Returned list not guaranteed
        in any particular order.

        Parameters:
         none

        Returns: list[str]
        '''
        raise NotImplementedError("todo: Trie.all_words")

    def num_words(self):
        '''
        Return the number of words in the trie.

        Parameters:
          none

        Returns: int
        '''
        raise NotImplementedError("todo: Trie.num_words")

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        raise NotImplementedError("todo: Trie.completions")

    def _compl(self, prefix, acc):
        '''
        Private method. Return all completions given prefix. The
        variable acc stores the string seen thus far in traversal of
        the trie. The returned list is not guaranteed to be in any
        particular order.

        Parameters:
          prefix : str
          acc : str

        Returns: list[str]
        '''
        raise NotImplementedError("todo: Trie.completions")

    def num_completions(self, prefix):
        '''
        Return the number of completions of the given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        raise NotImplementedError("todo: Trie.num_completions")


class TrieOrthographer:
    """
    Class for a trie-based orthographer
    """

    def __init__(self):
        '''
        Constructor

        Parameters:
          none

        Initialize dictionary of empty tries, one per letter.
        '''
        self.tries = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.tries[char] = Trie(char)

    def insert(self, word):
        '''
        Insert the word into the orthographer if it consists only of lowercase
        letters.

        Parameters:
          word : str

        Returns: (does not return a value)
        '''
        raise NotImplementedError("todo: TrieOrthographer.insert")

    def insert_from_file(self, filename):
        '''
        Read the named file, insert words (one per line in file).

        Parameters:
          filename : str

        Returns: (does not return a value)
        '''
        raise NotImplementedError("todo: TrieOrthographer.insert_from_file")

    def contains(self, word):
        '''
        Check presence of given word in the orthographer.

        Parameters:
          word : str

        Returns: boolean
        '''
        raise NotImplementedError("todo: TrieOrthographer.contains")

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        raise NotImplementedError("todo: TrieOrthographer.completions")

    def num_completions(self, prefix):
        '''
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        raise NotImplementedError("todo: TrieOrthographer.num_completions")

    def all_words(self):
        '''
        Return all the words in the orthographer. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        raise NotImplementedError("todo: TrieOrthographer.all_words")

    def num_words(self):
        '''
        Return the number of words in the orthographer.

        Parameters:
          none

        Returns: int
        '''
        raise NotImplementedError("todo: TrieOrthographer.num_words")
