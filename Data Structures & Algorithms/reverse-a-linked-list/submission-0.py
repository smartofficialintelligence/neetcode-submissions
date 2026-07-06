# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:   # base case: empty or last node
            return head
        newHead = self.reverseList(head.next)  # reverse the rest first
        head.next.next = head           # node ahead points back at me
        head.next = None                # cut my old forward link
        return newHead                  # same new head all the way up