# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Input: root = [1,2]
# Output: 1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        
        def depth(root):
            if not root: return 0
            left, right = depth(root.left), depth(root.right)
            self.best = max(self.best, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.best
            
        