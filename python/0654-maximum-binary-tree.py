# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.

# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]


# We want to optimize from O(n^2) time complexity, 
# O(nlogn) doesn't seem like very promising, so we try O(n). 
# Basically, if we need O(n) solution, 
# we can only have constant operation during the traverse of the list.
#  Therefore, we need something the keep track of the traversing memory. 
# We then brainstorm several data structures that can help us keep track of this kind of memory.

# What memory do we need? 
# We need to remember the max node rather than trying to find them each time. 
# So we need something that has an order and hierarchy. 
# Stack comes in very naturally for this need given its characteristics. 
# All we need to do is to force an order by ourselves.

# Time: O(n)
# Space: worst O(n) in the case that the list is sortedin descending order.

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
                
            if stack:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]
            