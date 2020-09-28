"""
https://www.scaler.com/academy/mentee-dashboard/classroom/problems-on-trees-trie-1859f6a6-461c-49c3-8263-e0aaeaeba900/#assignment
Minimum largest element
Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation.

Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Find the minimum possible largest element after B operations.



Problem Constraints
1 <= N <= 106
0 <= B <= 105
-105 <= A[i] <= 105



Input Format
First argument is an integer array A.
Second argument is an integer B.



Output Format
Return an integer denoting the minimum possible largest element after B operations.



Example Input
Input 1:

 A = [1, 2, 3, 4]
 B = 3
Input 2:

 A = [5, 1, 4, 2]
 B = 5


Example Output
Output 1:

 4
Output 2:

 5
"""

import heapq


class Solution:
    def solve(self, A, B):
        C = A.copy()
        heap = []
        for i in range(0, len(A)):
            heapq.heappush(heap, (A[i] * 2, i))

        while B:
            num = list(heapq.heappop(heap))
            C[num[1]] += A[num[1]]
            num[0] += A[num[1]]
            heapq.heappush(heap, tuple(num))
            B -= 1

        return max(C)


if __name__ == '__main__':
    A = [5, 1, 4, 2]
    print(Solution().solve(A, 3))
