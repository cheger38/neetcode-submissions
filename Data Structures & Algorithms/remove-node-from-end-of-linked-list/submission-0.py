# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        len = 0
        while cur:
            cur = cur.next
            len += 1
        
        print(len)
        if n == len:
            return head.next

        m = len - n
        cur = head
        while m > 1:
            m -= 1
            cur = cur.next

        cur.next = cur.next.next
        return head
            