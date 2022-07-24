# https://leetcode.com/problems/first-unique-character-in-a-string/

# Input: s = "loveleetcode"
# Output: 2

# Time: O(n)
# Space: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        d = collections.defaultdict(int)
        for char in s:
            d[char] += 1
        for i, char in enumerate(s):
            if d[char] < 2:
                return i
        return -1