# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Example:
# Input: [7,1,5,3,6,4]
# Output: (6 - 1) = 5

# Time: O(n)
# Space: O()
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxProfit = max(currentProfit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit

# Kadane's Algorithm
# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = maxProfit = 0
        for i in range(1, len(prices)):
            curProfit += prices[i] - prices[i - 1]
            if curProfit < 0:
                curProfit = 0
            maxProfit = max(curProfit, maxProfit)
        return maxProfit