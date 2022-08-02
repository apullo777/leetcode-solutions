# https://leetcode.com/problems/symmetric-tree/

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            outerPair = self.isMirror(left.left, right.right)
            innerPair = self.isMirror(left.right, right.left)
            return outerPair and innerPair
        else:
            return False