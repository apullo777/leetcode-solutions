# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# Time: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# iterative
# Time: O(n)

# visit the node of the tree in level order

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        list = deque([root])
        num_of_nodes = 1 # keep track of how many nodes for the current level
        levels = 0
        while list:
            node = list.popleft()
            if node.left:
                list.append(node.left)
            if node.right:
                list.append(node.right)
            num_of_nodes -= 1
            if num_of_nodes == 0:
                levels += 1
                num_of_nodes = len(list)
        return levels