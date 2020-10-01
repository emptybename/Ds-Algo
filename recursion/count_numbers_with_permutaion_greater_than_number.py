"""
There are some natural number whose all permutation is greater than or equal to that number eg. 123, whose all the permutation (123, 231, 321) are greater than or equal to 123.

Given a natural number n, the task is to count all such number from 1 to n.

Examples:

Input : n = 15.
Output : 14
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12,
13, 14, 15 are the numbers whose all
permutation is greater than the number
itself. So, output 14.

Input : n = 100.
Output : 54
"""


def countNumber(n):
    result = 0

    # Pushing 1 to 9 because all number
    # from 1 to 9 have this property.
    for i in range(1, 10):
        s = []
        if (i <= n):
            s.append(i)
            result += 1

        # take a number from stack and add
        # a digit smaller than last digit
        # of it.
        while len(s) != 0:
            tp = s[-1]
            s.pop()
            for j in range(tp % 10, 10):
                x = tp * 10 + j
                if (x <= n):
                    s.append(x)
                    result += 1

    return result


# Driver Code
if __name__ == '__main__':
    n = 15
    print(countNumber(n))
