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
        dict = collections.defaultdict(lambda: Node(0)) #makes dict; if doesn't exist in dict, Node(0) is its default val
        dict[None] = None
        curr = head

        while curr:
            dict[curr].val = curr.val
            dict[curr].next = dict[curr.next]
            dict[curr].random = dict[curr.random]
            curr = curr.next
        
        return dict[head]