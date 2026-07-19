"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        hash = dict()
        cur = head
        while cur:
            copy = Node(cur.val, None, cur.random)
            hash[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            if cur.next: hash[cur].next = hash[cur.next]   
            if cur.random: hash[cur].random = hash[cur.random]
            cur = cur.next

        return hash[head]



