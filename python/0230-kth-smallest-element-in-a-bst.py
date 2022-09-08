# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# DFS in-order recursive
# Time: O(n)
# Space: O()

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.found = False
        self.inorder(root)
        return self.res
        
    def inorder(self, node):
        # exit early when meet kth element
        if self.found: return 
        if not node: return 
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            self.found = True
            return 
        self.inorder(node.right)

# Pythonic solution using generator

def traverse(node):
    if node:
        yield from traverse(node.left)
        yield node
        yield from traverse(node.right)
    
def kthSmallest(root, k):
    k -= 1
    for i, node in enumerate(traverse(root)):
        if i == k:
            return node.val