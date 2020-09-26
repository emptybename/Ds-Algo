"""
https://www.interviewbit.com/problems/n-max-pair-combinations/

Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)
"""
from typing import List


class HeapNode:
    def __init__(self, ai: int, bj: int, val: int) -> None:
        self.ai = ai
        self.bj = bj
        self.val = val


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def push(self, heap_node: HeapNode) -> None:
        self.heap.append(heap_node)
        self.size += 1
        # Maintain heap property
        child = self.size - 1

        while child > 0:
            parent = (child - 1) // 2
            if self.heap[parent].val < self.heap[child].val:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent
            else:
                child = 0

    def heapify(self, start: int) -> None:
        largest = start
        left = 2 * start + 1
        right = 2 * start + 2

        if left < self.size and self.heap[left].val > self.heap[largest].val:
            largest = left

        if right < self.size and self.heap[right].val > self.heap[largest].val:
            largest = right

        if largest != start:
            self.heap[start], self.heap[largest] = self.heap[largest], self.heap[start]
            self.heapify(largest)

    def pop(self):
        if self.is_empty():
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.size -= 1
        node = self.heap.pop()
        # print(node)
        self.heapify(0)
        return node

    def replace(self, heap_node: HeapNode) -> None:
        self.heap[0] = heap_node
        self.heapify(0)


class Solution:
    def solve(self, a: List[int], b: List[int]) -> List[int]:
        ans = []
        _duplicate = {}
        a.sort(reverse=True)
        b.sort(reverse=True)
        n = len(a)
        heap = MaxHeap()
        heap.push(HeapNode(0, 0, a[0] + b[0]))
        _duplicate[(0, 0)] = True
        num = 0
        while num < n:
            node = heap.pop()
            ans.append(node.val)
            if node.bj + 1 < n and not _duplicate.get((node.ai, node.bj + 1), False):
                heap.push(HeapNode(node.ai, node.bj + 1, a[node.ai] + b[node.bj+1]))
                _duplicate[(node.ai, node.bj + 1)] = True

            if node.ai + 1 < n and not _duplicate.get((node.ai+1, node.bj), False):
                heap.push(HeapNode(node.ai+1, node.bj, a[node.ai+1] + b[node.bj]))
                _duplicate[(node.ai+1, node.bj)] = True
            num += 1
        return ans


if __name__ == '__main__':
    A= [36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20,
        12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37,
        -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16,
        14, -7, 0, 37, -42, 26, 28]
    B= [38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42,
        2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44,
        33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38,
        14, -22, -9, 0, 43]
    print(Solution().solve(A, B))
