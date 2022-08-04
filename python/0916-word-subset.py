# https://leetcode.com/problems/word-subsets/

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target = {}
        for word in words2:
            for char in word:
                count = word.count(char)
                if char not in target or count > target[char]:
                    target[char] = count
                    
        s = set(words1)
        for word in words1:
            for char in target:
                if word.count(char) < target[char]:
                    s.remove(word)
                    break
        return list(s)