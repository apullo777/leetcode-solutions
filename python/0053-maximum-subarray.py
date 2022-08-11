# https://leetcode.com/problems/maximum-subarray/

# Approach 1: Using 2 for loops
# Time: O(n^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list = []
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                list.append(sum)
        return max(list, default = 0)

# Approch 2: create a list storing the maximum of total or nums[i], traverse the list and return the maximum
# Time: O(n)
# Space: O(n)


# Dynamic Programing
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)
        return maxSum

# Divide and Conquer 
# Recurrence relation: T(N) = 2T(N/2) + O(N)
# Time: O(n log n)
# Space: O(log n) 

# divide the array into sub-problems on the left and right halves 
# and then combine these results on the way back up to find the maximum subarray sum.       

class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)

# Optimized Divide & Conquer
# Recurrence relation: T(N) = 2T(N/2) + O(1)
# Time: O(n)
# Space: O(n)

# The O(N) term in the recurrence relation of previous solution was due to computation of max sum subarray involving nums[mid] in each recursion.
# But we can reduce that term to O(1) if we precompute it. 

class Solution:
    def maxSubArray(self, nums):
        # pre[i] denotes the maximum subarray ending at i
        # suf[i] denotes the maximum subarray starting at i
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
        for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
        def maxSubArray(A, L, R):
            if L == R: return A[L]
            mid = (L + R) // 2
            return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
        return maxSubArray(nums, 0, len(nums)-1)