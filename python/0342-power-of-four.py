# https://leetcode.com/problems/power-of-four/

# Input: n = 16
# Output: true

# Input: n = 5
# Output: false

# Input: n = 1
# Output: true

# simple recursion

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # If n is 0, False
		# If n is 1, True
        if n < 2: return n == 1
        
        # Not divisible by 4, False
        if n % 4: return False

        return self.isPowerOfFour(n / 4)

# Simply check if the log is integer
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()
           
# bitwise manipulation:

# First we use n & (n - 1) to check whether n is power of 2.
# It works because a binary power of two is of the form 1000...000 
# and subtracting one will give you 111...111. 
# Then, when you AND those together, you get 0.

# Solution 1:
# We turn every power of 4 within 32 bit into binary form
# (Constraints: -23^1 <= n <= 2^31 - 1)
# We XOR them together, we will get:
# 1010101010101010101010101010101 (1431655765)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1)) and n & 1431655765 == n

# Solution 2:
# Since 4 is a square number, we will get a perfect integer using sqrt().

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not(n & (n-1)) and int(sqrt(n)) * int(sqrt(n)) == n