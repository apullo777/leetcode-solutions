# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

# Greedy solution 1

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = prev = 0
        for i in range(1, len(s)):
            if s[prev] != s[i]: prev = i
            else: 
                ans += min(cost[prev], cost[i])
                if cost[prev] < cost[i]: prev = i
        return ans

# solution 2
class Solution:
    def minCost(self, s, cost):
        ans = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            ans += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return ans