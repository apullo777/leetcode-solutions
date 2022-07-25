# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedList = None
        while head:
            head.next, reversedList, head = reversedList, head, head.next
        return reversedList 
        
# recursive
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node, head.next.next, head.next = self.reverseList(head.next), head, None
        return node
