# https://leetcode.com/problems/pacific-atlantic-water-flow/

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]

# DFS in matrix
# Starting from each point, and dfs its neighbor if the neighbor is equal or less than itself.
# And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. 
# Finally go through all nodes again and see if it can be both reached by two oceans. 
# The trick is if a node is already visited, no need to visited again.

# Time: O(m * n), each cell is visited once.
# Space: O(m * n + h) 
#        For each DFS we need O(h) space used by the system stack, 
#        where h is the maximum depth of the recursion. 
#        In the worst case, O(h) = O(m * n).
#        Each visited set can have at maximum all cells from the matrix so O(mn)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # 1. Check for an empty graph.
        if not matrix:
            return []
        
        # 2. Initialize
        rows, cols = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def traverse(i, j, visited):
            # a. Check if visited
            if (i, j) in visited:
                return 
            # b. Else add to visted
            visited.add((i, j))

            # c. Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)
                        
        # 3. For each point, traverse it.
        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)
            
        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)
            
        return list(p_visited & a_visited)