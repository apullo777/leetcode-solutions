# https://leetcode.com/problems/longest-increasing-subsequence/

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Input: nums = [0,1,0,3,2,3]
#Output: 4

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# DP
# Time: O(n^2)
# Space: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # Let dp[i] is the longest increase subsequence of nums[0..i] which has nums[i] as the end element of the subsequence.
        for i in range(n): # 
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


# 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        list = []
        for num in nums:
            idx = bisect.bisect_left(list, num)
            if idx == len(list):
                list.append(num)
            else:
                list[idx] = num
        return len(list)
        