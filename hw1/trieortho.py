"""
CMSC 14200: trie-based spell-checker and tab-completer Distribution

Adam Shaw
Winter 2023

Boris Fosso
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
        if(word[0]!=self.root):
          return
        
        if len(word)==1:
          self.final = True
          return

        for c in self.children.values():
          if c.root==word[1]:
            c.insert(word[1:])
            return

        newTrie = Trie(word[1])
        newTrie.insert(word[1:])
        self.children[len(self.children)] = newTrie

    def contains(self, word):
        '''
        Check presence of given word in the trie.

        Parameters:
         word : str

        Returns: boolean
        '''
        if len(word)==1:
          return self.final
        for c in self.children.values():
          if word[1]==c.root:
            return c.contains(word[1:])
        return False


    def all_words(self):
        '''
        Return all the words in the trie. Returned list not guaranteed
        in any particular order.

        Parameters:
         none

        Returns: list[str]
        '''

        t = self
        lstoTrie = []
        lstoBase = []
        final = []

        if self.final:
          final.append(self.root)

        for c in self.children.values():
          if c.final:
            final.append(self.root+c.root)
          if len(c.children)>0:
            lstoTrie.append(c)
            lstoBase.append(self.root+c.root)
        
        while(len(lstoTrie) > 0):
          c = lstoTrie.pop()
          base = lstoBase.pop()
          for cc in c.children.values():
            if(cc.final):
              final.append(base+cc.root)
            if len(cc.children)>0:
              lstoTrie.append(cc)
              lstoBase.append(base+cc.root)
        return final

    def num_words(self):
        '''
        Return the number of words in the trie.

        Parameters:
          none

        Returns: int
        '''

        count = 0
        if self.final:
          count = count + 1
        for c in self.children.values():
          count = count + c.num_words()
        return count

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        return self._compl(prefix, "")

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

        if(self.root!=prefix[0] and len(acc)==0):
          return []

        if len(prefix)==1:
          lst = self.all_words()
          final = []
          for i in lst:
            final.append(acc+i)
          return final

        for i in range(0, len(self.children)):
          c = self.children[i]
          print(c.root)
          if c.root==prefix[1]:
            return c._compl(prefix[1:], acc+self.root)
        return []

    def num_completions(self, prefix):
        '''
        Return the number of completions of the given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        if len(prefix)==1:
          return self.num_words()
        for i in range(0, len(self.children)):
          c = self.children[i]
          if(c.root==prefix[1]):
            return c.num_completions(prefix[1:])


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
        for c in word:
          if c not in "qwertyuiopasdfghjklzxcvbnm":
            return
        self.tries[word[0]].insert(word)

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

        for ln in file.readlines():
          word = ln.strip()
          self.insert(word)
        
        file.close()

    def contains(self, word):
        '''
        Check presence of given word in the orthographer.

        Parameters:
          word : str

        Returns: boolean
        '''
        return self.tries[word[0]].contains(word)

    def completions(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        return self.tries[prefix[0]].completions(prefix)

    def num_completions(self, prefix):
        '''
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        return self.tries[prefix[0]].num_completions(prefix)

    def all_words(self):
        '''
        Return all the words in the orthographer. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        all = []
        for tr in self.tries.values():
          for word in tr.all_words():
            all.append(word)
        return all

    def num_words(self):
        '''
        Return the number of words in the orthographer.

        Parameters:
          none

        Returns: int
        '''
        num = 0
        for tr in self.tries.values():
          num = num + tr.num_words()
        return num
