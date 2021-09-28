arr = [None] * (2 * 100001)
arr[0] = 1
freq = [None] * (2 * 100001)
freq[0] = {1: 1}

def get_count():

    # Initilize i to 1
    i = 1

    # Initilize p to 1 (i.e 2^i)
    # in each iteration
    # i will be pth power of 2
    p = 1

    # loop to generate gould's Sequence
    while i <= 100000:

        # i is pth power of 2
        # traverse the array
        # from j=0 to i i.e (2^p)
        j = 0

        while j < i:
            # double the value of arr[j]
            # and store to arr[i+j]
            num = 2 * arr[j]
            arr[i + j] = num
            # print(arr[i+j])
            freq[i + j] = freq[i + j - 1].copy()
            freq[i + j][num] = freq[i + j].get(num, 0) + 1
            j += 1

        # upadate i to next power of 2
        i = (1 << p)

        # increment p
        p += 1


if __name__ == '__main__':
    get_count()
    print(freq[8][2])
