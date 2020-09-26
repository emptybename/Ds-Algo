"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not
the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    l = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print(Solution().findKthLargest(l, 4))
