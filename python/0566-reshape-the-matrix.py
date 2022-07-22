# https://leetcode.com/problems/reshape-the-matrix/

# Input: nums = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatList = []
        matrix = []
        for sublist in nums:
            for item in sublist:
                flatList.append(item)
        if len(flatList) != r * c:
            return nums
        else:
            for i in range(0, len(flatList), c):
                matrix.append(flatList[i: i + c])
            return matrix