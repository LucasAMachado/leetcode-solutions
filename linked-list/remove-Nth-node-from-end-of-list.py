# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # shift the right pointer to the nth position
        while n > 0 and right:
            right = right.next
            n -= 1

        # shift the left and the right pointer until right is pointing to null
        while right:
            right = right.next
            left = left.next


        # remove the nth node
        left.next = left.next.next

        return dummy.next
