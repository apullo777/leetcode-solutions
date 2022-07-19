# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# hash table
# Time: O(m + n)
# Space: O(min(m, n))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        
        counter = Counter(nums1)
        list = []
        for num in nums2:
            if counter[num] > 0:
                list.append(num)
                counter[num] -= 1
        return list


# two pointers
# Time: O(n log n)
# Space: O(sorting)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        list = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                list.append(nums1[i])
                i += 1
                j += 1
        return list
                