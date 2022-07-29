# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def translate(word):
            dict = {}
            return [dict.setdefault(char, len(dict)) for char in word]
        translated = translate(pattern)
        return [word for word in words if translate(word) == translated]