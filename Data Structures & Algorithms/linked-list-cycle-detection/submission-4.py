# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tort = head  
        hare = head.next

        while tort and hare and hare.next:
            if tort == hare:
                return True
            
            tort = tort.next
            hare = hare.next.next

        return False