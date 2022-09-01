# https://leetcode.com/problems/reduce-array-size-to-the-half/

# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] 
# which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] 
# which has a size greater than half of the size of the old array.

# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. 
# This will make the new array empty.

# Greedy solution using counter and sorting
# Time: O(n log n)
# Space: O(n)

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        totalFrequency, size = 0, 0
        for frequency in sorted(cnt.values(), reverse = True):
            totalFrequency += frequency
            size += 1
            if totalFrequency >= len(arr) // 2: break
                
        return size
                
        