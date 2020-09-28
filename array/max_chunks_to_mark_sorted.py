"""
https://leetcode.com/problems/max-chunks-to-make-sorted/
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top < 0

    def push(self, ele):
        self.stack.append(ele)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            ele = self.stack.pop()
            self.top -= 1
        else:
            ele = None
        return ele

    def top_ele(self):
        return self.stack[-1]


class Solution:
    def solve(self, A):
        stack = Stack()
        for ele in A:
            if stack.is_empty():
                stack.push(ele)
            elif stack.top_ele() > ele:
                item = stack.top_ele()
                while not stack.is_empty() and stack.top_ele() > ele:
                    stack.pop()
                stack.push(item)
            else:
                stack.push(ele)
        return stack.top + 1


if __name__ == '__main__':
    arr = [3, 2, 2]
    print(Solution().solve(arr))
