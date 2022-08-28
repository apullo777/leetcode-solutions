# https://leetcode.com/problems/set-matrix-zeroes/

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# solution 1
# track if any row or any col has a zero, which means the entire row or col has to be zero

# Space: O(m + n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        zero_row = [False] * m
        zero_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_row[row] = True
                    zero_col[col] = True
                    
        for row in range(m):
            for col in range(n):
                if zero_row[row] or zero_col[col]:
                    matrix[row][col] = 0

# solution 2
# instead of having a separate array to track the zeroes, 
# we simply use the first row or col to track them and then 
# go back to update the first row and col with zeroes after we're done replacing it

# At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col.
# Then iterate through the array again to see where the first row and col were marked as zero and then set that row/col as 0.
# After doing that, you'll need to traverse through the first row and/or first col if there were any zeroes there to begin with and set everything to be equal to 0 in the first row and/or first col.

# Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
        
        zero_first_row = False
        zero_first_col = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        zero_first_row = True
                    if col == 0:
                        zero_first_col = True
                    matrix[row][0] = matrix[0][col] = 0
                    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[row][0] == 0 or matrix[0][col] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if zero_first_row:
            for col in range(n):
                matrix[0][col] = 0
        
        if zero_first_col:
            for row in range(m):
                matrix[row][0] = 0