# https://leetcode.com/problems/rotate-image/

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse
        left, right = 0, len(matrix) - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Pythonic: 
# using [::-1] to flip the matrix upside down and then zip to transpose it

class Solution:
    def rotate(self, A):
        A[:] = map(list, zip(*A[::-1]))

# explanation
# * is the splat operator. It is used for unpacking a list into arguments. 
# For example: foo(*[1, 2, 3]) is the same as foo(1, 2, 3).
# calling A = zip(*A) is returning:
# A = [[1, 2, 3], [4, 5, 6],[7, 8, 9,]]
# So zip(*A) is the same as calling zip([1, 2, 3], [4, 5, 6],[7, 8, 9,])
# It will yield:
#      (1, 4, 7)
#      (2, 5, 8)
#      (3, 6, 9)
# [[1st in 1st list, 1st in 2nd list,....], [2nd in 1st list, 2nd in 2nd list....], ....]
# It's exactly like transposing the matrix.

# And for the A[:] part, the difference is you are making a copy of the entire list
# If you only use A = zip(*A[::-1]), you just make A point to the new list
# If you use A[:] = zip(*A[::-1]), you actually assign the value to your A


# list comprehension

class Solution:
    def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]