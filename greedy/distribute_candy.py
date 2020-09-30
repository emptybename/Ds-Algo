"""
https://www.interviewbit.com/problems/distribute-candy/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Input Format:

The first and the only argument contains N integers in an array A.
Output Format:

Return an integer, representing the minimum candies to be given.
Example:

Input 1:
    A = [1, 2]

Output 1:
    3

Explanation 1:
    The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor.
    So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.

Input 2:
    A = [1, 5, 2, 1]

Output 2:
    7

Explanation 2:
    Candies given = [1, 2, 3, 4, 2, 1]
                    [1 3 4 4 3 2 1]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        alen = len(A)
        ans = [1]*alen
        stack = [0]
        size = 1
        for i in range(1, alen):
            if A[i] >= A[stack[-1]]:
                while size > 0:
                    item = stack.pop()
                    val = ans[item]
                    if item + 1 < alen and A[item] > A[item+1]:
                        val = max(val, ans[item+1] + 1)
                    if item - 1 >= 0 and A[item-1] < A[item]:
                        val = max(val, ans[item-1]+1)
                    ans[item] = val
                    size -= 1
            stack.append(i)
            size += 1
        while size > 0:
            # print("Yes")
            # print(stack)
            item = stack.pop()
            val = ans[item]
            if item + 1 < alen and A[item] > A[item + 1]:
                val = max(val, ans[item + 1] + 1)
            if item - 1 >= 0 and A[item - 1] < A[item]:
                val = max(val, ans[item - 1] + 1)
            ans[item] = val
            size -= 1
        # print(ans)
        # print(stack)
        return sum(ans)


if __name__ == '__main__':
    A = [1, 2, 4, 4, 3, 2, 1]
    print(Solution().candy(A))





