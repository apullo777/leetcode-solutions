# https://leetcode.com/problems/poor-pigs/

# Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
# Output: 5
# Example 2:

# Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
# Output: 2
# Example 3:

# Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
# Output: 2


# Observation 1: 
# If there are x pigs, they can represent (encode) 2^x buckets.
# Case 1: If the number of rounds is 1.
# Example: 4 buckets, 15 minutes to die, and 15 minutes to test. The answer is 2. 
# Suppose a bit represent a pig, the cases are: (00, 10, 01, 11).

# Observation 2:
# If there are r rounds, a (r + 1)-based number is used to represent (encode) the buckets. 
# That’s also why the first conclusion uses the 2-based number.
# Example: 8 buckets, 15 buckets to die, and 40 buckets to test. 
# Now, there are 2 (= (40/15).floor) attempts, as a result, 3-based number is used to encode the buckets. 
# The minimum number of pigs required are 2 (= Math.log(8, 3).ceil).

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie  
        return math.ceil(math.log(buckets, rounds + 1))  # each pig can provide log(rounds + 1, 2) bits of information, and locating the target needs log(buckets, 2) bits of information.