"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        heap = []
        keys = list(frequency.keys())
        i = 0
        while i < k:
            heap.append((frequency[keys[i]], keys[i]))
            # heapq.heappush(heap, (frequency[keys[i]], keys[i]))
            i += 1

        heapq.heapify(heap)

        while i < len(keys):
            if heap[0][0] < frequency[keys[i]]:
                heapq.heappop(heap)
                heapq.heappush(heap, (frequency[keys[i]], keys[i]))
            i += 1

        return [ele[1] for ele in heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution(). topKFrequent(nums, k))
