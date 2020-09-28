"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        heap_size = len(A)
        for node in A:
            heapq.heappush(heap, (node.val, node))
        node = heapq.heappop(heap)[1]
        heap_size -= 1
        head = node
        current = head
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
            heap_size += 1
        while heap_size > 0:
            node = heapq.heappop(heap)[1]
            heap_size -= 1
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
                heap_size += 1
            current.next = node
            current = current.next
        return head



"""
Note:  This problem can also be solved using divide-conquer. 
Solve the problem for first k/2 and last k/2 list. Then you have 2 sorted lists. Then simiply merge the lists.
Analyze the time complexity.
T(N) = 2 T(N/2) + N
T(N) = O (N log N)
"""
