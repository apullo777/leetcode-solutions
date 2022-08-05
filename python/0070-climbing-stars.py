# https://leetcode.com/problems/climbing-stairs/

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    # if we know the number ways to get to the points [n-1] and [n-2] respectively, denoted as n1 and n2, 
    # then the total ways to get to the point [n] is n1 + n2
    def climbStairs(self, n):
        toCurr = toNext = 1
        for i in range(n):
            toCurr, toNext = toNext, toCurr + toNext
        return toCurr