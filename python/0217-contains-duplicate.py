# https://leetcode.com/problems/contains-duplicate/

# using set()
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# using hashtable
# Time: O(n)
# Space: O(n)
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                return True
        return False

# using sort()
# Time: O(n log n)
# Space: O(1)
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# brute force
# Time: O(n^2)
# Space: O(1)
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False