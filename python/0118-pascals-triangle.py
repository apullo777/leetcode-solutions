# https://leetcode.com/problems/pascals-triangle/

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows= [[1]]
        for row in range(1, numRows):
            rows.append([1] * (row + 1))
            for col in range(1, row):
                rows[row][col] = rows[row - 1][col] + rows[row - 1][col - 1]
        return rows