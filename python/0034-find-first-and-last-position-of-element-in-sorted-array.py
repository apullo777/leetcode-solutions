# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [], target = 0
# Output: [-1,-1]

# Time: O(log n)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        
        def findIndex(target): # binary search 
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid 
            return low 
        
        low = findIndex(target) # leftmost idx of target
        high = findIndex(target + 1) - 1 # rightmost idx of target
        if low <= high: # there are at least one target
            return [low, high] 
        return [-1, -1]