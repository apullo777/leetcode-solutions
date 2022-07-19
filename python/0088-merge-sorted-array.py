# https://leetcode.com/problems/merge-sorted-array/

# Time: O(n)
# Space: O(1)

# Example:
# Input: [1,2,3,0,0,0], 3, [2,5,6], 3
# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
    