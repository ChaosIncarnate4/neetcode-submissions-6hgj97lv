# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalfStart = slow.next
        slow.next = None
        curr = secondHalfStart
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        firstCurr = head
        secondCurr = prev

        while secondCurr:
            nextNode = firstCurr.next
            nextSecondNode = secondCurr.next

            firstCurr.next = secondCurr
            secondCurr.next = nextNode

            firstCurr = nextNode
            secondCurr = nextSecondNode