# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Input: head = []
# Output: []

# mergesort
# Time: O(n log n)
# Space: O(log n)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, head1, head2):
        dummy = cur = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                cur.next, head1 = head1, head1.next
            else:
                cur.next, head2 = head2, head2.next
            cur = cur.next
        cur.next = head1 or head2
        return dummy.next

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?