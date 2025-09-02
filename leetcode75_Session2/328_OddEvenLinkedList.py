# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        firstEven = head.next
        odd = head
        even = head.next

        while odd.next or even.next:
            if even.next:
                odd.next = even.next
                odd = odd.next
            else:
                odd.next = firstEven
                break
            
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                odd.next = firstEven
                even.next = None
                break

        return head



