# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy = ListNode(None)
        rightDummy = ListNode(None)
        leftPointer, rightPointer = leftDummy, rightDummy
        while head:
            if head.val < x:
                leftPointer.next = head
                leftPointer = leftPointer.next
            else:
                rightPointer.next = head
                rightPointer = rightPointer.next
            head = head.next
        rightPointer.next = None
        leftPointer.next = rightDummy.next
        return leftDummy.next
        