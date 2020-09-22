"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

from typing import List, Set


class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    @staticmethod
    def get_node() -> TrieNode:
        return TrieNode()

    @staticmethod
    def char_to_index(char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = self.char_to_index(char)
            if node.children[index] is None:
                node.children[index] = self.get_node()
            node = node.children[index]
        node.is_end_of_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self.char_to_index(char)
            if node.children[index] is None:
                return False
        return True


class Solution:
    def __init__(self):
        self.trie = Trie()

    @staticmethod
    def is_valid_cell(board: List[List[str]], i: int, j: int, rows: int, cols: int) -> bool:
        return 0 <= i < rows and 0 <= j < cols and board[i][j] != "$"

    def find_word_from_board(
            self, board: List[List[str]], word: List[str], i: int, j: int, ans: Set[str], rows: int, cols: int,
            curr_node: TrieNode) -> None:
        index = Trie.char_to_index(word[-1])
        if curr_node.children[index] is None:
            return
        curr_node = curr_node.children[index]
        if curr_node.is_end_of_word:
            ans.add(''.join(word))
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if self.is_valid_cell(board, i + rowOffset, j + colOffset, rows, cols):
                letter = board[i + rowOffset][j + colOffset]
                word.append(letter)
                board[i + rowOffset][j + colOffset] = "$"
                self.find_word_from_board(board, word, i + rowOffset, j + colOffset, ans, rows, cols, curr_node)
                board[i + rowOffset][j + colOffset] = letter
                word.pop()

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.trie.insert(word)
        ans = set()
        rows = len(board)
        cols = len(board[0])
        # Using DFS we will check each possible word and add in ans
        for i in range(0, rows):
            for j in range(0, cols):
                letter = board[i][j]
                board[i][j] = "$"
                word = [letter]
                self.find_word_from_board(board, word, i, j, ans, rows, cols, self.trie.root)
                board[i][j] = letter
        return list(ans)


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().find_words(board, words))
