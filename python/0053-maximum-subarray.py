# https://leetcode.com/problems/maximum-subarray/

# Approach 1: Using 2 for loops
# Time: O(n^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list = []
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                list.append(sum)
        return max(list, default = 0)

# Approch 2: create a list storing the maximum of total or nums[i], traverse the list and return the maximum
# Time: O(n)
# Space: O(n)


# Dynamic Programing
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)
        return maxSum