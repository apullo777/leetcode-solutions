# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)"

# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, 
# except we cannot omit the first parenthesis pair 
# to break the one-to-one mapping relationship 
# between the input and the output.

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        left = '({})'.format(self.tree2str(root.left)) if (root.left or root.right) else ''
        right = '({})'.format(self.tree2str(root.right)) if root.right else ''
        return '{}{}{}'.format(root.val, left, right)