# https://leetcode.com/problems/missing-number/

# Input: nums = [3,0,1]
# Output: 2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(range(0, n + 1)) - sum(nums)
            