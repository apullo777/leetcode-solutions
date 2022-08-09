# https://leetcode.com/problems/range-sum-query-immutable/

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# create an array acc that stores the accumulated sum for nums
# return acc[right] - acc[left -1] in sumRange

# Time: O(n)
# Space: O(1)

class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = nums
        for i in range(len(nums) - 1):
            self.acc[i + 1] += self.acc[i] 
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.acc[right]
        return self.acc[right] - self.acc[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)