# https://leetcode.com/problems/product-of-array-except-self/

# Time: O(n)
# Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, ans = 1, 1, [1] * len(nums)
        for i in range(len(nums)):
            ans[i] *= pre     # prefix product from one end
            pre *= nums[i]
            ans[-1-i] *= suf  # suffix product from other end
            suf *= nums[-1-i]
        return ans