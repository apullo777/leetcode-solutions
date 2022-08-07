# https://leetcode.com/problems/find-the-duplicate-number/

# two pointers
# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
                
        # move slow pointer to the start and run them with the same speed and wait until they concide
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

# bit manipulation
# Time: O(n)
# Space: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            if bits & 1 << num:
                return num
            bits |= 1 << num