# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

# Input: matrix = [[-5]], k = 1
# Output: -5

# Solution 1: Max Heap keeps up to k elements

# iterate all elements in the matrix and and add elements into the maxHeap
# The maxHeap will keep up to k smallest elements 
# because when maxHeap is over size of k, we do remove the top of maxHeap which is the largest one
# Finally, the top of the maxHeap is the kth smallest element in the matrix

# Time: O(M * N * logK), where M <= 300 is the number of rows, N <= 300 is the number of columns.
# Space: O(K), space for heap which stores up to k elements.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        maxHeap = []
        for row in range(m):
            for col in range(n):
                heappush(maxHeap, -matrix[row][col])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)

# Solution 2: Min Heap to find kth smallest element from amongst N sorted list

# we can understand the problem as finding the kth smallest element from amongst M sorted rows.
# start the pointers to point to the beginning of each rows, 
# then we iterate k times, for each time ith, 
# the top of the minHeap is the ith smallest element in the matrix.
# We pop the top from the minHeap then add the next element which has the same row with that top to the minHeap

# Time: O(K * logK)
# Space: O(K)

class Solution:  
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  
        minHeap = []  # val, row, col  
        for row in range(min(k, m)):
            heappush(minHeap, (matrix[row][0], row, 0))

        ans = -1  # any dummy value
        for i in range(k):
            ans, row, col = heappop(minHeap)
            if col + 1 < n: 
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))
        return ans
