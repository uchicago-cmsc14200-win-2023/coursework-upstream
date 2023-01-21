"""
CMSC 14200, Winter 2023
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math


class MinHeap:
    @staticmethod
    def parent_index(i):
        if i == 0:
            return None
        return (i - 1) // 2

    @staticmethod
    def left_child_index(i):
        return 2 * i + 1

    @staticmethod
    def right_child_index(i):
        return 2 * i + 2

    def __init__(self, max_capacity=999):
        self.data = [None] * max_capacity
        self.next = 0

    def size(self):
        return self.next

    def height(self):
        return math.floor(math.log(self.next, 2)) + 1

    def is_empty(self):
        return self.next == 0

    def reset(self):
        self.next = 0

    def min(self):
        if self.is_empty():
            return None
        return self.data[0]

    def _swap(self, p, q):
        assert p < self.next and q < self.next
        tmp = self.data[p]
        self.data[p] = self.data[q]
        self.data[q] = tmp

    def _sift_up(self, pos):
        if pos == 0:
            return
        pi = MinHeap.parent_index(pos)
        if self.data[pos] < self.data[pi]:
            self._swap(pos, pi)
            self._sift_up(pi)

    def _sift_down(self, pos):
        curr = self.data[pos]
        li = MinHeap.left_child_index(pos)
        ri = MinHeap.right_child_index(pos)

        if li >= self.next:
            return

        if li < self.next and ri >= self.next:
            lc = self.data[li]
            m = min(curr, lc)
            if lc == m:
                self._swap(pos, li)
                self._sift_down(li)
        else:
            (lc, rc) = (self.data[li], self.data[ri])
            m = min([curr, lc, rc])
            if rc == m:
                self._swap(pos, ri)
                self._sift_down(ri)
            elif lc == m:
                self._swap(pos, li)
                self._sift_down(li)

    def remove_min(self):
        if self.is_empty():
            return None
        min_item = self.data[0]
        if self.next > 0:
            self.data[0] = self.data[self.next - 1]
            self.next -= 1
            self._sift_down(0)
        return min_item

    def insert(self, n):
        self.data[self.next] = n
        self.next += 1
        self._sift_up(self.next - 1)

    def _verify(self, pos):
        if pos >= self.next:
            return True
        curr = self.data[pos]
        li = MinHeap.left_child_index(pos)
        ri = MinHeap.right_child_index(pos)
        if ri < self.next:
            return (
                curr <= self.data[ri]
                and curr <= self.data[li]
                and self._verify(ri)
                and self._verify(li)
            )
        if li < self.next:
            return curr <= self.data[li] and self._verify(li)
        return True

    def verify(self):
        return self._verify(0)

    def show(self):
        if self.is_empty():
            print("[empty]")
            return
        linebreak = 1
        row_count = 0
        for i in range(self.next):
            print(self.data[i], end=" ")
            row_count += 1
            if row_count == linebreak or i == self.next - 1:
                print()
                linebreak *= 2
                row_count = 0
