# https://leetcode.com/problems/word-search/

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# brute force DFS backtracking
# Time: O(m * n * 3^k), where k is length of word and m and n are sizes of our board
# Space: O(k)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        def dfs(idx, i, j):
            if self.found: 
                return  # early stop if word is found 
            if idx == k:
                self.found = True  # for early stop
                return 
            if i < 0 or i >= m or j < 0 or j >= n: return 
            tmp = board[i][j]
            if tmp != word[idx]: return 
            
            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(idx + 1, i + x, j + y)
            board[i][j] = tmp
            
        for i, j in product(range(m), range(n)):
            if self.found: return True  # early stop if word is found
            dfs(0, i, j)
            
        return self.found