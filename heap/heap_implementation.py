"""
https://www.geeksforgeeks.org/building-heap-from-array/?ref=rp
Building Heap from Array
Given an array of N elements. The task is to build a Binary Heap from the given array. The heap can be either Max Heap
or Min Heap.
"""
from typing import List


def max_heapify(arr: List[int], n: int, i: int) -> None:
    """ Heapify subtree rooted with node i in arr """

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)


def build_max_heap(arr: List[int], n: int) -> None:
    """
    heapify for all non leaf nodes
    """
    start = n // 2 - 1
    for i in range(start, -1, -1):
        max_heapify(arr, n, i)


def min_heapify(arr: List[int], n: int, i: int) -> None:
    """ Heapify subtree rooted with node i in arr """
    # if i * 2 + 1 >= n:
    #     return
    smallest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, n, smallest)


def build_min_heap(arr: List[int], n: int) -> None:
    """
    heapify for all non leaf nodes
    """
    start = n // 2 - 1
    for i in range(start, -1, -1):
        min_heapify(arr, n, i)


def heap_sort_increasing(arr: List[int], n: int) -> None:
    """Sort array in increasing order using max heap"""
    build_max_heap(arr, n)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def heap_sort_decreasing(arr: List[int], n: int) -> None:
    """Sort array in increasing order using max heap"""
    build_min_heap(arr, n)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)


def print_heap(arr: List[int], n: int) -> None:
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17]
    n = len(arr)
    # build_max_heap(arr, n)
    # print_heap(arr, n)
    # print()
    # heap_sort_increasing(arr, n)
    # print_heap(arr, n)
    # print()
    # build_min_heap(arr, n)
    # print_heap(arr, n)

    heap_sort_decreasing(arr, n)
    print_heap(arr, n)
