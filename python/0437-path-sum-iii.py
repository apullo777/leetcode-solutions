# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global res
        res = 0
        self.dfs(root, targetSum)
        return res
        
    def dfs(self, root, targetSum):
        global res
        if not root: return
        if root.val == targetSum:
            res += 1
        self.findPath(root.left, targetSum - root.val)
        self.findPath(root.right, targetSum - root.val)