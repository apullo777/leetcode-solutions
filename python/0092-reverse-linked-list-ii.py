# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Input: head = [5], left = 1, right = 1
# Output: [5]

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        l = dummy = ListNode(None)
        dummy.next = head
        for i in range(left - 1): l = l.next
        tail = l.next
        
        for i in range(right - left):
            tmp = l.next    # next
            l.next = tail.next
            tail.next = tail.next.next
            l.next.next = tmp
            
        return dummy.next
        
        