'''
Figured it out. About 30 minutes.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 2
        reversePrev = ListNode(head.val)
        reverseCurr = ListNode(head.next.val, reversePrev)
        reverseNext = None

        curr = head.next
        
        while curr.next:
            curr = curr.next
            reversePrev = reverseCurr
            reverseCurr = ListNode(curr.val, reversePrev)
            n += 1
        
        maxTwinSum = 0
        curr = head
        while n > 0:
            # print(curr.val, reverseCurr.val)
            maxTwinSum = max(maxTwinSum, curr.val + reverseCurr.val)

            curr = curr.next
            reverseCurr = reverseCurr.next
            n -= 2
        
        return maxTwinSum

            
            
            

            
        
