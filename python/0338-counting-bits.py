# https://leetcode.com/problems/counting-bits/

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Time: O(n)
# Space: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0]
        for i in range(1, n + 1):
            # any number will have the same bit count as half that number, 
            # with an extra one if it's an odd number
            cnt.append(cnt[i >> 1] + i % 2) 
        return cnt

# Base 2: 111    Base 10: 7    
# Base 2: 1110   Base 10: 14  
# Base 2: 11100  Base 10: 28 
# Base 2: 11101  Base 10: 29