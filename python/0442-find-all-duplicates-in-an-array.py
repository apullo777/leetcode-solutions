# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# Input: nums = [1,1,2]
# Output: [1]

# Input: nums = [1]
# Output: []

# The idea is we do a linear pass using the input array itself 
# as a hash to store which numbers have been seen before. 
# We do this by making elements at certain indexes negative.

# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans