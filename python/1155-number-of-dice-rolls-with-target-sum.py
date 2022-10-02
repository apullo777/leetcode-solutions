# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.

# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 109 + 7.

# DP with memoization
# As an initial example, pretend we have 5 dice with 6 faces each and we want to determine how many ways to make 18.
# In other words, what is dp(5, 6, 18)?
# This die can take on f=6 different values (1 to 6), 
# so we consider what happens when we fix its value to each possibility (6 cases):

# Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1=17. This can happen dp(4, 6, 17) ways.
# Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2=16. This can happen dp(4, 6, 16) ways.
# Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3=15. This can happen dp(4, 6, 15) ways.
# Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4=14. This can happen dp(4, 6, 14) ways.
# Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5=13. This can happen dp(4, 6, 13) ways.
# Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6=12. This can happen dp(4, 6, 12) ways.

# dp(5, 6, 18) = dp(4, 6, 17) + dp(4, 6, 16) + dp(4, 6, 15) + dp(4, 6, 14) + dp(4, 6, 13) + dp(4, 6, 12)

# The general relation is:
# dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)

class Solution:
    def numRollsToTarget(self, d, f, t):
        dp = {}
        def r_roll(dice, target):
            if target > f * dice:
                dp[dice, target] = 0
                return 0
            if dice == 0: return target==0
            if target < 0: return 0
            if (dice, target) in dp: return dp[dice, target]
            ways = 0
            for num in range(1, f+1):
                ways += r_roll(dice-1, target-num)
            dp[dice, target] = ways
            return ways
        return r_roll(d, t) % (10**9+7)