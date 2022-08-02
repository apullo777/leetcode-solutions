# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# preorder
# repeatedly shift the left subtree to the right while preserving the order
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                p = curr.left
                # shift the right subtree to the right most point in the left subtree
                while p.right:
                    p = p.right
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right