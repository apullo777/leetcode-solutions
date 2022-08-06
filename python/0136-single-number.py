# https://leetcode.com/problems/single-number/

# Input: nums = [4,1,2,1,2]
# Output: 4

# Xor / Bit Manipulation
# Time: O(n)
# Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

# dictionary
# Time: O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for num, i in cnt.items():
            if i < 2:
                return num

# sum 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)