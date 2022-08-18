# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Time: O(n)
# Space: O(1)

# For list [1,2,3,4,5,6,7] we need to return [1,7,2,6,3,5,4]. 
# We can note, that it is actually two lists [1,2,3,4] and [7,6,5], where elements are interchange. 
# So, to succeed we divide the probelm into three steps:

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find mid point
        if not head: return []
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nxt = curr.next  # store the next node
            curr.next = prev  # reverse node relation
            prev = curr # update prev and curr
            curr = nxt
        slow.next = None
        
        # step 3: merge lists
        head1, head2 = head, prev
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next
            head1.next = head2
            head1 = nxt1
            head2.next = head1
            head2 = nxt2