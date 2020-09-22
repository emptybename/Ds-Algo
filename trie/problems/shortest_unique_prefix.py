"""
https://www.interviewbit.com/problems/shortest-unique-prefix/

Given a list of N words. Find shortest unique prefix to represent each word in the list.

Input Format
First and only argument is a string array of size N.

Output Format
Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.

input:
A = ["zebra", "dog", "duck", "dove"]
output:
["z", "dog", "du", "dov"]

"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        # self.is_end_of_word = False Not required
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _get_char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        trie = self.root
        for ch in word:
            idx = self._get_char_to_index(ch)
            if trie.children[idx] is None:
                trie.children[idx] = TrieNode()
            trie = trie.children[idx]
            trie.count += 1

    def get_unique_prefix(self, word):
        unique = []
        trie = self.root
        for ch in word:
            idx = self._get_char_to_index(ch)
            unique.append(ch)
            trie = trie.children[idx]
            if trie.count == 1:
                return ''.join(unique)
        return ''.join(unique)


class Solution(list):
    # @param A : list of strings
    # @return a list of strings
    def __int__(self, words):
        for word in words:
            self.append(word)

    def prefix(self):
        root = Trie()
        for word in self:
            root.insert(word)
        ans = []
        for word in self:
            ans.append(root.get_unique_prefix(word))
        return ans


if __name__ == '__main__':
    A = ["zebra", "dog", "duck", "dove"]
    solution = Solution(A)
    print(solution.prefix())
    B = ["apple", "ball", "cat"]
    solution = Solution(B)
    print(solution.prefix())
