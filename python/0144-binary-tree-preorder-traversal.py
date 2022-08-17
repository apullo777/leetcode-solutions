# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, list = [root], []
        while stack:
            node = stack.pop()
            if node:
                list.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return list

# recursive - 1
class Solution:
    def preorderTraversal1(self, root):
        list = []
        self.dfs(root, list)
        return list
    
    def dfs(self, root, list):
        if root:
            list.append(root.val)
            self.dfs(root.left, list)
            self.dfs(root.right, list)

# recursive - 2
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # [1] + [2] + [] = [1,2] is how the logic works
        list = []
        if root:
            list += [root.val]
            list += self.preorderTraversal(root.left)
            list += self.preorderTraversal(root.right)
        return list