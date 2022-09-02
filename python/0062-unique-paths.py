# https://leetcode.com/problems/unique-paths/

# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, 
# there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# DP - Memoization
# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i >= m or j >= n: return 0 # beyond boundaries
            # only one way to reach the bottom-right corner from bottom-right corner
            if i == m - 1 and j == n - 1: return 1 
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0, 0)

# DP - Tabulation
# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# DP - Space optimized
# A common way in dp problems to optimize space from 2d dp 
# is just to convert the dp matrix from m x n grid to 2 x n grid 
# denoting the values for current and previous row. 
# We can just overwrite the previous row and use the current row as the previous row for next iteration.

# Time: O(m * n)
# Space: O(n)

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for i in range(2)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j-1]
        return dp[(m - 1) & 1][-1]

# Or still better yet, in this case, you can use a single vector as well. 
# We are only accessing same column from previous row 
# which can be given by dp[j] and previous column of current row 
# which can be given by dp[j-1]

class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j-1]
        return dp[-1]