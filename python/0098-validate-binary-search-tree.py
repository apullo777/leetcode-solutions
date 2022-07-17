# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution 
class Solution:
    def isValidBST(self, root, lessThan = float('inf'), greaterThan = float('-inf')): 
        if not root:
            return True
        if root.val <= greaterThan or root.val >= lessThan:
            return False
        # recursively check the left and right subtree of the current one
        return self.isValidBST(root.left, min(root.val, lessThan), greaterThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, greaterThan))

# in-order traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        self.traverse(root, nodes)
        return len(nodes) == len(set(nodes)) and nodes == sorted(nodes) 

    def traverse(self, root: Optional[TreeNode], nodes: List[int]):
        if root:
            self.traverse(root.left, nodes)
            nodes.append(root.val)
            self.traverse(root.right, nodes)

