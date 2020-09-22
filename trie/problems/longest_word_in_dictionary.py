"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
one character at a time by other words in words. If there is more than one possible answer, return the longest word
with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller
than "apply".
"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            # if node.children[idx] is None:
            #     return False
            node = node.children[idx]
            if not node.is_end_of_word:
                return False
        return True


class Solution:
    def longest_word(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = ""
        ansLen = 0
        for word in words:
            if trie.search(word):
                wLen = len(word)
                if ansLen < wLen or (ansLen == wLen and ans > word):
                    ans = word
                    ansLen = wLen
        return ans


if __name__ == '__main__':
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    solution = Solution()
    print(solution.longest_word(words))