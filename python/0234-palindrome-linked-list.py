# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [1,2,2,1]
# Output: true

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:     
            fast = fast.next.next
            slow = slow.next    # find the mid node
        rev = None
        while slow:      # reverse the second half
            slow.next, rev, slow = rev, slow, slow.next
        while rev:      # compare the first and second half nodes
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True