# https://leetcode.com/problems/find-and-replace-pattern/

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def translate(word):
            dict = {}
            return [dict.setdefault(char, len(dict)) for char in word]
        translated = translate(pattern)
        return [word for word in words if translate(word) == translated]