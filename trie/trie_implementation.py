class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end_of_word = False

    def is_empty(self) -> bool:
        for node in self.children:
            if node is not None:
                return False
        return True


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def _get_node(self) -> TrieNode:
        return TrieNode()

    def _get_char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        trie = self.root
        for ch in word:
            idx = self._get_char_to_index(ch)
            if trie.children[idx] is None:
                trie.children[idx] = self._get_node()
            trie = trie.children[idx]
        trie.is_end_of_word = True

    def search(self, word: str) -> bool:
        trie = self.root
        for ch in word:
            idx = self._get_char_to_index(ch)
            if trie.children[idx] is None:
                return False
            trie = trie.children[idx]
        return trie.is_end_of_word

    def delete(self, root: TrieNode,  word: str, size: int, depth: int) -> TrieNode:
        if root is None:
            return root

        if size == depth:
            root.is_end_of_word = False
            return root

        idx = self._get_char_to_index(word[depth])
        root.children[idx] = self.delete(
            root.children[idx], word, size, depth+1
        )

        if root.is_empty() and not root.is_end_of_word:
            return None

        return root


def main():
    words = ["mayank", "ankit", "shivhare"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    if trie.search('mayank'):
        print("mayank is present")
    else:
        print("mayank is not present")
    if trie.search('hello'):
        print("hello is present")
    else:
        print("hello is not present")

    if trie.search('mayan'):
        print("mayan is present")
    else:
        print("mayan is not present")

    if trie.search('shivhare'):
        print("shivhare is present")
    else:
        print("shivhare is not present")

    print("Deleting Shivhare")
    trie.delete(trie.root, 'shivhare', 8, 0)

    if trie.search('shivhare'):
        print("shivhare is present")
    else:
        print("shivhare is not present")

    print("Inserting shiv")
    trie.insert("shiv")
    print("Inserting shivhare")
    trie.insert("shivhare")

    print("deleting shiv")
    trie.delete(trie.root, 'shiv', 4, 0)

    if trie.search('shivhare'):
        print("shivhare is present")
    else:
        print("shivhare is not present")
    print("Inserting shiv")
    trie.insert("shiv")
    print("Deleting Shivhare")
    trie.delete(trie.root, 'shivhare', 8, 0)

    if trie.search('shiv'):
        print("shiv is present")
    else:
        print("shiv is not present")


if __name__ == '__main__':
    main()
