"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 2


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, bits: List[int]) -> None:
        node = self.root
        for i in range(0, len(bits)):
            idx = bits[i]
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def max_xor(self, bits: List[int]) -> int:
        xor = 0
        node = self.root
        i = 31
        for bit in bits:
            if bit and node.children[0] is not None:
                # xor.append(1)
                xor += 2 ** i
                node = node.children[0]
            elif bit:
                # xor.append(0)
                node = node.children[1]
            elif not bit and node.children[1] is not None:
                # xor.append(1)
                xor += 2 ** i
                node = node.children[1]
            elif not bit:
                # xor.append(0)
                node = node.children[0]
            i -= 1
        return xor


class Solution:
    @staticmethod
    def convert_num_to_binary(num: int) -> List[int]:
        bits = [0] * 32
        i = 31
        while num > 0:
            bits[i] = num % 2
            num = num // 2
            i -= 1
        return bits

    def find_maximum_xor(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        trie = Trie()
        for num in nums:
            bits = self.convert_num_to_binary(num)
            trie.insert(bits)
        ans = 0
        for num in nums:
            bits = self.convert_num_to_binary(num)
            ans = max(ans, trie.max_xor(bits))
        return ans


if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    solution = Solution()
    print(solution.find_maximum_xor(nums))
