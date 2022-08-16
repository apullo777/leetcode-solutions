
# https://leetcode.com/problems/count-vowels-permutation/

# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
 
# Input: n = 5
# Output: 68

# Bottom up DP
# Each vowel allows some number of subsequent characters. These transitions are like a tree. 
# This problem is asking, "what's the width of the tree with height n?"
# This solution keeps track of the number of each vowel at a level in this tree. 
# To calculate say 'A', we calculate how many nodes in the previous level produce 'A'. 
# This is the number of 'E', 'I', and 'U' nodes.

# Time: O(n)
# Space: O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e +i + o + u) % (10 ** 9 + 7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n :
            return 0
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a  # Here's starting from back of the string, so that we can use mappings directly from the description without having to translate it in our minds.
        return (a + e +i + o + u) % (10 ** 9 + 7)

# Top down DP / DFS
# Let dfs to try all possible result. When we reach a valid possible way, return 1. 
# Use memoization to cache the sub-problem result, so it doesn't need compute again.

class Solution:  
    def countVowelPermutation(self, n: int) -> int:
        map = {
            '.': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        @lru_cache(None)
        def dp(i, last):
            if i == n: return 1
            ans = 0
            for nxt in map[last]:
                ans = (ans + dp(i + 1, nxt)) % (10 ** 9 + 7)
            return ans

        return dp(0, '.')