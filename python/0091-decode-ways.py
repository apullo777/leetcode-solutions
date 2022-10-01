# https://leetcode.com/problems/decode-ways/

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

# Problem Reduction: variation of n-th staircase with n = [1, 2] steps.
# if we know the number ways to get to the digit s[i-1] and s[i-2] respectively,
# then the total ways to get to the point s[i] is s[i-1] + s[i-2]

# buttom up DP
# The tricky part is handling the corner cases (e.g. s = "30").
# Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].
# Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

# For example:
# s = "231"
# index 0: extra base offset. dp[0] = 1
# index 1: # of ways to parse "2" => dp[1] = 1
# index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
# index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': 
            return 0
        dp = [0 for _ in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]
        
        for i in range(2, len(s) + 1):
            # one digit jump
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i-1]
            # two digit jump
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[-1]