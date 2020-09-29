"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        # print(rows, cols)
        _duplicate = {}
        # print(matrix[0][0])
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        _duplicate[(0, 0)] = True
        ans = -1
        while k > 0:
            ele = heapq.heappop(heap)
            # print(ele)
            ans = ele[0]
            i = ele[1]
            j = ele[2]
            if j + 1 < cols and not _duplicate.get((i, j + 1), False):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                _duplicate[(i, j + 1)] = True
            if i + 1 < rows and not _duplicate.get((i + 1, j), False):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                _duplicate[(i + 1, j)] = True
            k -= 1
            # print(ans)
        return ans


if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ],
    k = 8
    print(Solution().kthSmallest(matrix[0], k))
