'''
Reverse Linked List
'''

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mainFunction(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
      
class MyTests(unittest.TestCase):
    s = Solution()
    mainFunction = s.mainFunction

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

        actual = self.mainFunction(n)
        self.assertEqual(self.linkedListToList(actual), [5,4,3,2,1])

    def test2(self):
        listN = [1,2]
        n = self.createLinkedList(listN)

        actual = self.mainFunction(n)
        self.assertEqual(self.linkedListToList(actual), [2,1])

    def test3(self):
        listN = []
        n = self.createLinkedList(listN)

        actual = self.mainFunction(n)
        self.assertEqual(self.linkedListToList(actual), [])

unittest.main()