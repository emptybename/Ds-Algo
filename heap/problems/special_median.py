"""
https://www.scaler.com/academy/mentee-dashboard/classroom/heaps-bae7b539-aac1-4d4e-9850-f5752d04445b/#homework

You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
Median is the middle element in the sorted list of elements. If the number of elements are even then median will be (sum of both middle elements)/2.

Return 1 if the array is special else return 0.

NOTE:

For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]


Problem Constraints
1 <= N <= 1000000.
A[i] is in the range of a signed 32-bit integer.



Input Format
First and only argument is an integer array A.



Output Format
Return 1 if the given array is special else return 0.



Example Input
Input 1:

 A = [4, 6, 8, 4]
Input 2:

 A = [2, 7, 3, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explantion 1:

 Here, 6 is equal to the median of [8, 4].
Explanation 2:

 No element satisfies any condition.
"""

import heapq
from abc import ABC, abstractmethod


class Heap(ABC):

    @abstractmethod
    def push(self, item): pass

    @abstractmethod
    def pop(self): pass

    @abstractmethod
    def top(self): pass


class MinHeap(Heap):
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, item):
        heapq.heappush(self.heap, item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]


class MaxHeap(Heap):
    def __init__(self, size):
        self.heap = [None] * size
        self.size = 0

    def push(self, item):
        self.heap[self.size] = item
        self.size += 1

        # maintain heap
        child = self.size - 1
        while child > 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent
            else:
                child = 0

    def heapify(self, start):
        largest = start
        left = 2 * start + 1
        right = 2 * start + 2

        if left < self.size and self.heap[largest] < self.heap[left]:
            largest = left

        if right < self.size and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != start:
            self.heap[largest], self.heap[start] = self.heap[start], self.heap[largest]
            self.heapify(largest)

    def pop(self):
        item = self.top()
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return item

    def top(self):
        return self.heap[0]


class Solution:

    @staticmethod
    def get_median(A, alen):
        left_arr = [A[0]]
        min_heap = MinHeap()
        max_heap = MaxHeap(alen)
        max_heap.push(A[0])
        for i in range(1, alen):
            if A[i] > left_arr[-1]:
                min_heap.push(A[i])
            else:
                max_heap.push(A[i])
            if min_heap.size - max_heap.size > 1:
                item = min_heap.pop()
                max_heap.push(item)
            elif max_heap.size - min_heap.size > 1:
                item = max_heap.pop()
                min_heap.push(item)

            if max_heap.size > min_heap.size:
                left_arr.append(max_heap.top())
            elif min_heap.size > max_heap.size:
                left_arr.append(min_heap.top())
            else:
                mid = (min_heap.top() + max_heap.top()) / 2
                left_arr.append(mid)
        return left_arr

    def solve(self, A):
        alen = len(A)
        if alen == 0:
            return 0
        B = A.copy()
        B.reverse()
        left_arr = self.get_median(A, alen)
        right_arr = self.get_median(B, alen)
        right_arr.reverse()

        # print(left_arr)

        for i in range(0, alen):
            if i > 0 and left_arr[i - 1] == A[i]:
                return 1
            if i < alen - 1 and right_arr[i + 1] == A[i]:
                return 1
        return 0


if __name__ == '__main__':
    A = [2, 7, 3, 1]
    print(Solution().solve(A))
