from heapq import merge
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
    
        # Use a merge sort method to merge pairs of lists (paris of 2)
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # list2 may be out of bounds if len(lists) % 2 == 1 thus we need safety check 
                mergedLists.append(self.merge_two_linked_lists(l1, l2))
            
            lists = mergedLists
            
        return lists[0]
        
    # Helper to merge two linked lists
    def merge_two_linked_lists(self, list1, list2):
        # implement this function 
        dummy = ListNode()
        tail = dummy 
        
        while list1 and list2:
            
            if list1.val < list2.val:
              tail.next = list1
              list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next