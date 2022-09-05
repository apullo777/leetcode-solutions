# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Input: root = [1,2,3], targetSum = 5
# Output: []

# Input: root = [1,2], targetSum = 0
# Output: []

# DFS + recursion

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    
    def dfs(self, root, targetSum, path, res):
        if not root: return 
        if not root.left and not root.right and root.val == targetSum:
            path.append(root.val)
            res.append(path)
            
        self.dfs(root.left, targetSum - root.val, path + [root.val], res)
        self.dfs(root.right, targetSum - root.val, path + [root.val], res)

# DFS + stack

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        stack = [(root, targetSum, [])]

        while stack:
            curr, val, path = stack.pop()

            if not curr.left and not curr.right and val == curr.val:
                res.append(path + [curr.val])
            if curr.left:
                stack.append((curr.left, val - curr.val, path + [curr.val]))
            if curr.right:
                stack.append((curr.right, val - curr.val, path + [curr.val]))

        return res

# BFS + queue

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        from collections import deque
        queue = deque([(root, targetSum, [])])
        
        while queue:
            curr, val, path = queue.popleft()
            if not curr.left and not curr.right and val == curr.val:
                res.append(path + [curr.val])
                
            if curr.left:
                queue.append((curr.left, val - curr.val, path + [curr.val]))
            if curr.right:
                queue.append((curr.right, val - curr.val, path + [curr.val]))
            
        return res