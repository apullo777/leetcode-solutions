# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # filter the list to get all the unvisited indexes
        return [i + 1 for i, num in enumerate(nums) if num > 0]