# https://leetcode.com/problems/valid-anagram/

# Input: s1 = "anagram", s2 = "nagaram"
# Output: true

# Time: O(n)

class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] += 1
        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] += 1
        j = 0
        isValid = True
        while j < 26 and isValid:
            if c1[j] == c2[j]:
                j += 1
            else:
                isValid = False
        return isValid