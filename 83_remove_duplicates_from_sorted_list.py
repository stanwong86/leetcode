import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(unittest.TestCase):
    def deleteDuplicates(self, head) -> ListNode:
        root = head
        while head:
            # print(head.val)
            if head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                    continue
            head = head.next
        return root

    def convertToListNode(self, values):
        root = head = ListNode()
        for i, v in enumerate(values):
            head.val = v
            if i < len(values)-1:
                head.next = ListNode()
            head = head.next
        return root

    def convertToList(self, node):
        actual = []
        while node:
            actual.append(node.val)
            node = node.next
        return actual

    def test1(self):
        values = [1,1,2]
        expected = [1,2]

        head = self.convertToListNode(values)

        node = self.deleteDuplicates(head)

        self.assertTrue(isinstance(node, ListNode))
        
        actual = self.convertToList(node)
        self.assertEqual(actual, expected)

    def test2(self):
        values = [1,1,2,3,3]
        expected = [1,2,3]

        head = self.convertToListNode(values)

        node = self.deleteDuplicates(head)

        self.assertTrue(isinstance(node, ListNode))
        
        actual = self.convertToList(node)
        self.assertEqual(actual, expected)

unittest.main()
# unittest.main(Solution().test1())