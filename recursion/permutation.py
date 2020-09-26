"""
https://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
"""


def _permutations(ans, a, b, ai, bi, ansi, a_len, b_len):
    if ai == a_len and bi == b_len:
        print(''.join(ans))

    if ai < a_len:
        ans[ansi] = a[ai]
        _permutations(ans, a, b, ai + 1, bi, ansi + 1, a_len, b_len)

    if bi < b_len:
        ans[ansi] = b[bi]
        _permutations(ans, a, b, ai, bi + 1, ansi + 1, a_len, b_len)


def print_permutations(a, b):
    a_len = len(a)
    b_len = len(b)
    ans = [None] * (a_len + b_len)
    _permutations(ans, a, b, 0, 0, 0, a_len, b_len)


if __name__ == '__main__':
    a = "AB"
    b = "CD"
    print_permutations(a, b)
