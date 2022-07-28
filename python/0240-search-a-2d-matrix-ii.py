# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Input: matrix = [[1,4,7,11,15],
#                  [2,5,8,12,19],
#                  [3,6,9,16,22],
#                  [10,13,14,17,24],
#                  [18,21,23,26,30]], target = 5
# Output: true


# Time: O(m+n)
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start with element on the top right corner 
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y < len(matrix):
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True
        return False