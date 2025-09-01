# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        
        prev = None
        slow = head
        fast = head.next

        while fast and fast.next:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

            fast = fast.next.next
        
        # slow is the end of the first set
        twin = slow.next
        slow.next = prev

        res = 0
        while slow:
            print(slow.val, twin.val)
            res = max(res, slow.val + twin.val)
            slow = slow.next
            twin = twin.next
        
        return res