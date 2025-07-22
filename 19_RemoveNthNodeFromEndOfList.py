# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy 
        right = head
        
        # Create the buffer between L and R. This is the distance of n.
        while n > 0 and right: 
            right = right.next 
            n -= 1
        
        # Move Left and Right nodes together
        while right: 
            left = left.next 
            right = right.next
        
        # Next Left node is n because Right node is end of list.
        left.next = left.next.next 
        return dummy.next
        

