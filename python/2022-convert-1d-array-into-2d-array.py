# https://leetcode.com/problems/convert-1d-array-into-2d-array/

# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]

# Input: original = [1,2,3], m = 1, n = 3
# Output: [[1,2,3]]

# Input: original = [1,2], m = 1, n = 1
# Output: []

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        l = len(original)
        if l == m * n:
            for i in range(0, l, n):
                ans.append(original[i:i+n])
        return ans