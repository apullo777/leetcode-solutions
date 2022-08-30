# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# recursive
# Time: O(m * n)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isMatch(self, root, subRoot):
        if not (root and subRoot):
            return root is subRoot
        return (root.val == subRoot.val and
               self.isMatch(root.left, subRoot.left) and
               self.isMatch(root.right, subRoot.right))

# Merkle hashing
# For each node in a tree, we can create node.merkle, a hash representing it's subtree.
# This hash is formed by hashing the concatenation of 
# the merkle of the left child, the node's value, and the merkle of the right child. 
# Then, two trees are identical if and only if 
# the merkle hash of their roots are equal (except when there is a hash collision.)
# From there, finding the answer is straightforward: 
# we simply check if any node in s has node.merkle == t.merkle

# Time: O(m + n)

def isSubtree(self, s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()
        
    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle
        
    merkle(s)
    merkle(t)
    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or 
                dfs(node.left) or dfs(node.right))
                    
    return dfs(s)