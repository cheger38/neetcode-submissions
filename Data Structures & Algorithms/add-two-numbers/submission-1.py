# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = 0
        mult = 1
        cur = l1
        while cur:
            l1_sum += mult * cur.val
            mult *= 10
            cur = cur.next
        
        l2_sum = 0
        mult = 1
        cur = l2
        while cur:
            l2_sum += mult * cur.val
            mult *= 10
            cur = cur.next

        sum = l1_sum + l2_sum
        if sum == 0: return ListNode(0)
        
        dummy = ListNode()
        cur = dummy
        while sum > 0:
            new_node = ListNode(val=sum%10)
            sum //= 10
            cur.next = new_node
            cur = cur.next

        return dummy.next


