# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Example:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution 
# Time: O(n^2) 
from logging import root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0)) # pop() O(n)
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root

# iterative solution 
# TIme: O(n)
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
            
        root = TreeNode(preorder[0])
        stack = [root]
        i = 1
        j = 0
        
        # order of adding node: left -> 
        while i < len(preorder):
            temp = None
            node = TreeNode(preorder[i])
            # check if the latest node in stack is a left child node
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            # add right child node
            if temp:
                temp.right = node
            # add left child node
            else:
                stack[-1].left = node
            # next iteration
            stack.append(node)
            i += 1
        return root
