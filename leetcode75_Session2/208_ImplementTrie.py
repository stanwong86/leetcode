class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        letters = self.trie
        for ch in word: # a p p l e *
            if ch not in letters:
                letters[ch] = {}
            
            letters = letters[ch]
        
        letters['*'] = '*'

    def search(self, word: str) -> bool:
        letters = self.trie
        for ch in word:
            if ch not in letters:
                return False
            letters = letters[ch]
        
        return '*' in letters

    def startsWith(self, prefix: str) -> bool:
        letters = self.trie
        for ch in prefix:
            if ch not in letters:
                return False
            letters = letters[ch]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)