# https://leetcode.com/problems/combination-sum-iv/

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# we just need the counts, not the actual combinations


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for num in nums:
            if num <= target:
                dp[num] = 1  # Initialize the DP array to be 1 for each number in nums (since you can trivially make that total by just using that number itself)
        for sub_target in range(target + 1): 
            for num in nums:
                if sub_target - num > 0:
                    dp[sub_target] += dp[sub_target - num]
        return dp[-1]

# the core isea is to see how many ways we can make sub_target by taking each number num in nums and checking 
# how many ways we were able to make (sub_target - num) then adding that to the DP entry for sub_target.

# Step 1:
# sub_target = 1
# sub_target - 1 = 0 so add nothing
# sub_target - 2 < 0 so add nothing
# sub_target - 3 < 0 so add nothing
# DP = [0, 1, 1, 1, 0]

# Step 2:
# sub_target = 2
# sub_target - 1 = 1 so DP[2] += DP[1] and is now 2
# sub_target - 2 = 0 so add nothing
# sub_target - 3 < 0 so add nothing
# DP = [0, 1, 2, 1, 0]

# Step 3:
# sub_target = 3
# sub_target - 1 = 2 so DP[3] += DP[2] and is now 3
# sub_target - 2 = 1 so DP[3] += DP[1] and is now 4
# sub_target - 3 = 0 so add nothing
# DP = [0, 1, 2, 4, 0]

# Step 4:
# sub_target = 4
# sub_target - 1 = 3 so DP[4] += DP[3] and is now 4
# sub_target - 2 = 2 so DP[4] += DP[2] and is now 6
# sub_target - 3 = 1 so DP[4] += DP[1] and is now 7
# DP = [0, 1, 2, 4, 7]