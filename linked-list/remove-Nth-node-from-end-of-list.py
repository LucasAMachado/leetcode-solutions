# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        before = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            before = before.next
            ahead = ahead.next

        before.next = before.next.next

        return dummy.next
