# https://leetcode.com/problems/minimum-size-subarray-sum/

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# sliding window
# Time: O(n)
# SPace: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = 0
        result = len(nums) + 1
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0