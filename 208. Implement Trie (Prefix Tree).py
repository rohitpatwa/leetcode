# Use dictionary. Insert char as a key and it's next char as it's value. Mark end as a flag at the end of each word.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.d
        for c in word:
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]
        ptr['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.d
        for c in word:
            if c not in ptr:
                return False
            else:
                ptr = ptr[c]
        if 'end' in ptr:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.d
        for c in prefix:
            if c not in ptr:
                return False
            else:
                ptr = ptr[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)