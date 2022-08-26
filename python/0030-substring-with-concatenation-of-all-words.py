# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

# Using a counter and a sliding window, we push the window from left to right, 
# counting the number of valid words in the window. 
# When the number of a word in the window is more than the times it appears in words or we meet a invalid word, push the window.

from collections import Counter
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        m = len(words)
        n = len(words[0])
        ans = []
        total_length = m * n
        
        # loop over word length
        for k in range(n):
            left = k 
            sub_dict = defaultdict(int)
            count = 0
            # loop over the string
            for j in range(k, len(s) - n + 1, n):
                # get a word from observed substring
                word = s[j:j+n]
                # check if it is a valid word
                if word in cnt:
                    sub_dict[word] += 1
                    count += 1
                    # Shift the window as long as we have encountered more number of a word than is needed
                    # Note that we can shift the window by word length directly as the outer loop is there to
                    # make sure that anything is not missed out
                    # This solution will give indices out of order by OJ accepts it.
                    while sub_dict[word] > cnt[word]:
                        sub_dict[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    ##Count will be equal to m only when all the words are read the exact number of times needed
                    if count == m:
                        ans.append(left)
                #If is not a valid word then just skip over the current word (Don't worry about the middle characters 
                ##outer loop will take care of it)
                else:
                    left = j + n
                    sub_dict = defaultdict(int)
                    count = 0
        return ans
                        
        