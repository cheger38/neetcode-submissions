# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next


        l1 = head
        l2 = prev

        prev = ListNode(-1, None)
        dummy = prev
        while l2:
            print(l1.val, l2.val)
            prev.next = l1
            tmp = l1.next
            prev.next.next = l2
            prev = l2
            l1 = tmp
            l2 = l2.next

        prev.next = l1
        if prev.next:
            prev.next.next = None




            


       


