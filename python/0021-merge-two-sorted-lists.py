# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

# recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2

# in-place, iterative      
class Solution:
    def mergeTwoLists(self, list1, list2):
        if None in (list1, list2):
            return list1 or list2
        dummy = cur = ListNode(0)
        dummy.next = list1
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            else:
                nxt = cur.next
                cur.next = list2
                tmp = list2.next
                list2.next = nxt
                list2 = tmp
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next