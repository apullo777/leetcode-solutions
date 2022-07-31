# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# Time: O(n)
# Space: O(n)
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, result = deque(), []
        if root:
            q.append(root)
        while len(q):
            level = []
            for nodesOfCurrLevel in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result

# DFS
# Time: O(n)
# Space: O(n + h)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if not root:
            return 
        if len(result) <= level:
            result.append([]) # add a sublist to trace elemetns for the current level
        result[level].append(root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
