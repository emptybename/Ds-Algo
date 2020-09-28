"""
https://www.interviewbit.com/problems/magician-and-chocolates/

Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that kid can eat in A units of time.

NOTE:

floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7


Problem Constraints
1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 105



Input Format
First argument is an integer A.
Second argument is an integer array B of size N.



Output Format
Return an integer denoting the maximum number of chocolates that kid can eat in A units of time.



Example Input
Input 1:

 A = 3
 B = [6, 5]
Input 2:

 A = 5
 b = [2, 4, 6, 8, 10]


Example Output
Output 1:

 14
Output 2:

 33
"""

import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        heap = []
        for ele in B:
            ele *= -1
            heapq.heappush(heap, ele)
        ans = 0
        while A:
            num = (heapq.heappop(heap))*-1
            ans += num
            num = num//2 * -1
            heapq.heappush(heap, num)
            A -= 1
            ans %= 1000000007
        return ans


if __name__ == '__main__':
    A = 5
    B = [2, 4, 6, 8, 10]
    print(Solution().nchoc(A, B))
