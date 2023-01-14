"""
CMSC 14200: list-based spell-checker and tab-completer Distribution

Adam Shaw
Winter 2023

Boris Fosso
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
        for c in word:
          if c not in "qwertyuiopasdfghjklzxcvbnm":
            return
        for wrd in self.words:
          if wrd == word:
            return
        self.words.append(word)
          

    def insert_from_file(self, filename):
        '''
        Read the named file, insert words (one per line in file).

        Parameters:
          filename : str

        Returns: (does not return a value)
        '''
        try:
          file = open(filename, "r")
        except:
          print("File Not Found")
          return
        
        [self.insert(ln.strip()) for ln in file.readlines()]
        
        file.close()

    def contains(self, word):
        '''
        Check presence of given word in the orthographer.

        Parameters:
          word : str

        Returns: boolean
        '''
        for wrd in self.words:
          if wrd==word:
            return True
        
        return False

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        lst = []

        for wrd in self.words:
          if len(wrd) < len(prefix):
            pass
          elif wrd[0:len(prefix)] == prefix:
            lst.append(wrd)

        return lst

    def num_completions(self, prefix):
        '''
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        return len(self.completions(prefix))

    def all_words(self):
        '''
        Return all the words in the orthographer. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        return self.words

    def num_words(self):
        '''
        Return the number of words in the orthographer.

        Parameters:
          none

        Returns: int
        '''
        return len(self.words)

