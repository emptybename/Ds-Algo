"""
https://www.scaler.com/academy/mentee-dashboard/classroom/heaps-bae7b539-aac1-4d4e-9850-f5752d04445b/#assignment
Ayush has recently joined InterviewBit Academy as TA (Teaching Assistant). He has been assigned a job to keep record of all the errors each student is having in his batch and report it to the Mentor.

Since, the mentor gives extra attention to weak students, he resolves the issues of student having maximum number of errors first. But, to keep equality among students, he gives one minute to each student to resolve one of his errors and then ask the TA for next student.

Also, the lecture would not last more than B minutes and whenever a student has no more errors left, he leaves the lecture immediately.

Ayush, being confused each time, needs your help to shout out the roll number of student who should be helped at any time i.
You are given an array of integers, where A[i] denotes number of errors in code of student with roll number i.
Return a list containing the roll numbers,where element at index i denotes the roll number to be helped at minute i.
Ayush should keep on shouting roll numbers unless the B minutes are over or, the class is empty(everyone has left).

HINT: The returning array size will depend on the time till which roll numbers are shouted.

NOTE

1. Roll Numbers are 0-indexed (i.e, Roll numbers start from 0)

2. In case of tie(same number of errors), the least roll number is given preference.

3. There is no restriction on spending more than one minute consecutively on one student, as far as the mentor's condtions are met

4. Your code will be run on multiple test cases(<=10), try to come up with optimised solution.

Constraints

1 <= Number of Students <= 10^6
0 <= A[i] : Errors for each student <= 10^5
0 <= Sum of All Errors <= 10^6
1 <= B <= 10^6
Sample Input

4 2 5 3 6
4
Sample Output

4 2 4 0
Explanation

At i-th minute, the roll number to be help is announced :
0th minute: Roll 4 is having 6 errors
1st minute: Roll 2 and 4 are having 5 errors
2nd minute: Roll 4 is having 5 errors
3rd minute: Roll 0, 2 and 4 are having 4 errors
4th minute: Lecture ends!
So output would be [4 2 4 0]
"""


class HeapNode:
    def __init__(self, index, val):
        self.index = index
        self.val = val


class Heap:
    def __init__(self, size):
        self.heap = [None] * size
        self.size = size

    def add_node(self, index, heap_node):
        self.heap[index] = heap_node

    def heapify(self, start):
        largest = start
        left = 2 * start + 1
        right = 2 * start + 2
        left_condition = (
            left < self.size and (
                self.heap[largest].val < self.heap[left].val or (
                    self.heap[largest].val == self.heap[left].val and (
                        self.heap[largest].index > self.heap[left].index
                    )
                )
            )
        )
        if left_condition:
            largest = left

        right_condition = (
            right < self.size and (
                self.heap[largest].val < self.heap[right].val or (
                    self.heap[largest].val == self.heap[right].val and (
                        self.heap[largest].index > self.heap[right].index
                    )
                )
            )
        )

        if right_condition:
            largest = right

        if largest != start:
            self.heap[largest], self.heap[start] = self.heap[start], self.heap[largest]
            self.heapify(largest)

    def build(self):
        start = (self.size - 1)//2
        for i in range(start, -1, -1):
            self.heapify(i)

    def replace(self, node):
        self.heap[0] = node
        self.heapify(0)


class Solution:
    def solve(self, A, B):
        alen = len(A)
        heap = Heap(alen)
        for i in range(0, alen):
            # heap.heap[i] = HeapNode(i, A[i])
            heap.add_node(i, HeapNode(i, A[i]))
        heap.build()
        ans = []
        for i in range(0, B):
            if heap.heap[0].val <= 0:
                break
            ans.append(heap.heap[0].index)
            heap.replace(HeapNode(heap.heap[0].index, heap.heap[0].val - 1))
        return ans


if __name__ == '__main__':
    A = [4, 2, 5, 3, 6]
    B = 4
    print(Solution().solve(A, B))
