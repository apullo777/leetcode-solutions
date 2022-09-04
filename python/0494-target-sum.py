# https://leetcode.com/problems/target-sum/

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Input: nums = [1], target = 1
# Output: 1

# DP solution using DFS and memoization

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        idx = len(nums) - 1
        currSum = 0
        self.memo = {}
        return self.dfs(nums, target, idx, currSum)
    
    def dfs(self, nums, target, idx, currSum):
        if (idx, currSum) in self.memo:  # avoid repetitive computation
            return self.memo[(idx, currSum)]
        if idx < 0 and currSum == target: # valid: idx is out of bounds AND currSum is equal to target
            return 1
        if idx < 0: return 0  # invalid: Index is out of bounds
        
        # decisions: Should we add the current number positive or negative value?
        positive = self.dfs(nums, target, idx-1, currSum + nums[idx])
        negative = self.dfs(nums, target, idx-1, currSum - nums[idx])
        self.memo[(idx, currSum)] = positive + negative
        
        return self.memo[(idx, currSum)]  