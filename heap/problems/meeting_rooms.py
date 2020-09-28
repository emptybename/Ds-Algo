"""
https://www.interviewbit.com/problems/meeting-rooms/
Problem Description

Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.
Find the minimum number of conference rooms required so that all meetings can be done.



Problem Constraints
1 <= N <= 10

0 <= A[i][0] < A[i][1] <= 2 * 109



Input Format
The only argument given is the matrix A.

Output Format
Return the minimum number of conference rooms required so that all meetings can be done.

Example Input
Input 1:

 A = [      [0, 30]
            [5, 10]
            [15, 20]
     ]

Input 2:

 A =  [     [1, 18]
            [18, 23]
            [15, 29]
            [4, 15]
            [2, 11]
            [5, 13]
      ]

Example Output
Output 1:

 2
Output 2:

 4
"""

import heapq


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: x[0])
        heap = []
        heap_size = 0
        for start, end in A:
            if heap_size == 0:
                heapq.heappush(heap, end)
                heap_size += 1
            elif start < heap[0]:
                heapq.heappush(heap, end)
                heap_size += 1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
        return heap_size


if __name__ == '__main__':
    A = [
        [0, 30],
        [5, 10],
        [15, 20]
    ]
    print(Solution().solve(A))
