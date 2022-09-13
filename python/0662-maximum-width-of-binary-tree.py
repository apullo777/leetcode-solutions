# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The main idea with this question is we will give each node a position value. 
# If we go down the left neighbor, then position -> position * 2; 
# and if we go down the right neighbor, then position -> position * 2 + 1. 
# The width will be R (rightmost node) - L (leftmost) + 1.

# DFS solution

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we only store the most left node in the dict
        left, self.ans = {}, 0
        def dfs(root, level = 0, pos = 0):
            if root:
                if level not in left:
                    left[level] = pos
                self.ans = max(self.ans, pos - left[level] + 1)
                dfs(root.left, level + 1, pos * 2)
                dfs(root.right, level + 1, pos * 2 + 1)
        dfs(root)
        return self.ans
                
# Pythonic solution using enumerate()

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [child
                    for pos, node in level
                    for child in enumerate((node.left, node.right), pos * 2)
                    if child[1]]
        return width