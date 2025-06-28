'''
# Phase 1
o
1>2>3>4>5>6
  e

# Phase 2
  o
1>3
2>4>5>6
  e
# Phase 3
    o
1>3>5
2>4>6
    e

# Phase 4 - exit loop
1>3>5>2>4>6
'''

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        firstEven = head.next
        odd = head
        even = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # End of odd list points to first even of list
        odd.next = firstEven

        return head

class MyTests(unittest.TestCase):
    s = Solution()

    def createLinkedList(self, values: list):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linkedListToList(self, head: Optional[ListNode]) -> list:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test1(self):
        listN = [1,2,3,4,5]
        n = self.createLinkedList(listN)

        actual = self.s.oddEvenList(n)
        self.assertEqual(self.linkedListToList(actual), [1,3,5,2,4])

    def test2(self):
        listN = [2,1,3,5,6,4,7]
        n = self.createLinkedList(listN)

        actual = self.s.oddEvenList(n)
        self.assertEqual(self.linkedListToList(actual), [2,3,6,7,1,5,4])

    def test3(self):
        listN = [2,1,3,5,6,4,7,8]
        n = self.createLinkedList(listN)

        actual = self.s.oddEvenList(n)
        self.assertEqual(self.linkedListToList(actual), [2,3,6,7,1,5,4,8])

unittest.main()