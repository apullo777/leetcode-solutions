# https://leetcode.com/problems/search-a-2d-matrix/

# treat it as a sorted list instead of a 2D matrix
# it is basically an advanced version of binary search
# but if we flatten the the matrix it will have O(m * n) complexity, so we use virtual flatten
# if we need the number i element from our virtual flattened list, 
# it coresponds to element matrix[i // column][i % column] in our matrix.

# Time: O(log m * n)
# Space: O(1) 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        col, row = len(matrix[0]), len(matrix)
        low, high = 0, (col * row - 1)
        while low < high:
            mid = (low + high) // 2
            if matrix[mid // col][mid % col] < target:
                low = mid + 1
            else:
                high = mid
        return matrix[low // col][low % col] == target