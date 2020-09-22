"""
https://leetcode.com/problems/implement-trie-prefix-tree/
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    @staticmethod
    def char_to_index(ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            idx = self.char_to_index(ch)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            idx = self.char_to_index(ch)
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        if node.is_end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            idx = self.char_to_index(ch)
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
