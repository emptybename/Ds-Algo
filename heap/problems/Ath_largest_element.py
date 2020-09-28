"""
https://www.scaler.com/academy/mentee-dashboard/classroom/problems-on-trees-trie-1859f6a6-461c-49c3-8263-e0aaeaeba900/#homework
Ath largest element
Problem Description

Given an integer array B of size N.

You need to find the Ath largest element in the subarray [1 to i] where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].

NOTE: If any subarray [1 : i] has less than A elements then output array should be -1 at the ith index.



Problem Constraints
1 <= N <= 100000
1 <= A <= N
1 <= B[i] <= INT_MAX



Input Format
First argument is an integer A.
Second argument is an integer array B of size N.



Output Format
Return an integer array C, where C[i] (1 <= i <= N) will have the Ath largest element in the subarray [1 : i].



Example Input
Input 1:

 A = 4
 B = [1 2 3 4 5 6]
Input 2:

 A = 2
 B = [15, 20, 99, 1]


Example Output
Output 1:

 [-1, -1, -1, 1, 2, 3]
Output 2:

 [-1, 15, 20, 20]
"""

import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        blen = len(B)
        ans = [-1] * blen
        i = A
        heap = B[0:A]
        heapq.heapify(heap)
        ans[A - 1] = heap[0]
        while i < blen:
            if B[i] > heap[0]:
                heapq.heapreplace(heap, B[i])
            ans[i] = heap[0]
            i += 1
        return ans


if __name__ == '__main__':
    A = 2
    B = [15, 20, 99, 1]
    print(Solution().solve(A, B))
