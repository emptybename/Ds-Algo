"""
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
"""

from typing import List


class HeapNode:
    def __init__(self, word: str, frequency: int) -> None:
        self.word = word
        self.frequency = frequency


class Heap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    @staticmethod
    def compare_node(nodex: HeapNode, nodey: HeapNode) -> bool:
        if nodex.frequency < nodey.frequency:
            return True
        elif nodex.frequency > nodey.frequency:
            return False
        elif nodex.word > nodey.word:
            return True
        else:
            return False

    def heapify(self, start: int) -> None:
        largest = start
        left = start * 2 + 1
        right = start * 2 + 2

        if left < self.size and self.compare_node(self.heap[left], self.heap[largest]):
            largest = left

        if right < self.size and self.compare_node(self.heap[right], self.heap[largest]):
            largest = right

        if largest != start:
            self.heap[largest], self.heap[start] = self.heap[start], self.heap[largest]
            self.heapify(largest)

    def build(self) -> None:
        start = (self.size - 1) // 2
        for i in range(start, -1, -1):
            self.heapify(i)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        heap = Heap()
        keys = list(frequency.keys())
        i = 0
        while i < k:
            heap.heap.append(HeapNode(keys[i], frequency[keys[i]]))
            heap.size += 1
            i += 1

        heap.build()
        while i < len(keys):
            if heap.heap[0].frequency < frequency[keys[i]] or (
                    heap.heap[0].frequency == frequency[keys[i]] and heap.heap[0].word > keys[i]
            ):
                heap.heap[0] = HeapNode(keys[i], frequency[keys[i]])
                heap.heapify(0)
            i += 1
        heap.heap.sort(key=lambda x: (-x.frequency, x.word))
        return [heap_node.word for heap_node in heap.heap]


if __name__ == '__main__':
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(Solution().topKFrequent(words, k))
