"""
https://www.scaler.com/academy/mentee-dashboard/classroom/heaps-bae7b539-aac1-4d4e-9850-f5752d04445b/#assignment

Given an array of integers A denoting a stream of integers. New arrays of integer B and C are formed. Each time an integer is encountered in a stream, append it at the end of B and append median of array B at the C.

Find and return the array C.

NOTE:

If the number of elements are N in B and N is odd then consider medain as B[N/2] ( B must be in sorted order).
If the number of elements are N in B and N is even then consider medain as B[N/2-1]. ( B must be in sorted order).


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return an integer array C, C[i] denotes the median of first i elements.



Example Input
Input 1:

 A = [1, 2, 5, 4, 3]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 [1, 1, 2, 2, 3]
Output 2:

 [5, 5, 17, 11]

"""
import heapq
from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self):
        self.heap = []
        self.size = 0

    @abstractmethod
    def push(self, item): pass

    @abstractmethod
    def pop(self): pass

    @abstractmethod
    def top(self): pass


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def push(self, item):
        heapq.heappush(self.heap, item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def push(self, item):
        heapq.heappush(self.heap, item*-1)
        self.size += 1

    def pop(self):
        self.size -= 1
        return (heapq.heappop(self.heap)) * -1

    def top(self):
        return self.heap[0] * -1


class Solution:
    def solve(self, A):
        alen = len(A)
        if alen == 0:
            return []
        min_heap = MinHeap()
        max_heap = MaxHeap()
        ans = [A[0]]
        max_heap.push(A[0])
        for i in range(1, alen):
            if A[i] > ans[-1]:
                min_heap.push(A[i])
            else:
                max_heap.push(A[i])
            if min_heap.size > max_heap.size and min_heap.size - max_heap.size > 1:
                item = min_heap.pop()
                max_heap.push(item)
            elif max_heap.size > min_heap.size and max_heap.size - min_heap.size > 1:
                item = max_heap.pop()
                min_heap.push(item)

            if max_heap.size >= min_heap.size:
                ans.append(max_heap.top())
            else:
                ans.append(min_heap.top())
        return ans


if __name__ == '__main__':
    A = [5, 17, 100, 11]
    print(Solution().solve(A))
