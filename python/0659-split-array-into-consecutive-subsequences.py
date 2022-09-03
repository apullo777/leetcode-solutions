# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5

# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5

# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into 
# consecutive increasing subsequences of length 3 or more.

# Greedy solution using hashmap

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # left[i] denotes the number of i that I haven't placed yet.
        # end[i] denotes the number of consecutive subsequences that ends at number i.
        left, end = collections.Counter(nums), collections.Counter()
        
        for num in nums:
            if not left[num]: continue

            left[num] -= 1 # starting number

            if end[num - 1] > 0:  # add a num to the end of an existing valid subsequence
                end[num - 1] -= 1
                end[num] += 1

            elif left[num + 1] and left[num + 2]:  # form a valid subsequence
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
                
            else: return False
            
        return True