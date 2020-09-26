"""
https://www.geeksforgeeks.org/python-heapq-find-kth-smallest-element-2d-array/?ref=rp

"""

from typing import List


class MaxHeap:
    def __init__(self, arr: List[int]) -> None:
        self.heap = arr
        self.size = len(arr)

    def heapify(self, start: int) -> None:
        largest = start
        left = start * 2 + 1
        right = start * 2 + 2
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != start:
            self.heap[largest], self.heap[start] = (self.heap[start], self.heap[largest]
                                                    )
            self.heapify(largest)

    def build(self) -> None:
        start = self.size // 2 - 1
        for i in range(start, -1, -1):
            # print("Heapify is happening", i)
            self.heapify(i)

    def replace(self, ele):
        self.heap[0] = ele
        self.heapify(0)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li = []
        li_size = 0
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        # print(rows, cols)
        while i < rows:
            while j < cols:
                li.append(matrix[i][j])
                li_size += 1
                if li_size == k:
                    j += 1
                    break
                j += 1
            if li_size == k:
                # print("bahar", li_size, k)
                break
            i += 1
            j = 0
        heapq = MaxHeap(li)
        heapq.build()
        print(heapq.heap)
        print("i, j = ", i, j)
        while i < rows:
            while j < cols:
                # print(matrix[i][j], heapq.heap[0])
                if matrix[i][j] < heapq.heap[0]:
                    heapq.replace(matrix[i][j])
                j += 1
            i += 1
            j = 0
        return heapq.heap[0]


if __name__ == '__main__':
    arr = [[1, 2], [3, 3]]
    k = 3
    print(Solution().kthSmallest(arr, k))





