# https://leetcode.com/problems/mirror-reflection/

# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

# Input: p = 3, q = 1
# Output: 1

# Because the ray will hit one of the corners eventually 
# so the total height the ray traveled equals to the total height of stacked boxes. 
# We have this equation:
# s * p = r * q
# s = number of stacked boxes
# r = number of reflecting times

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # If p and q are both even, they are the multiples of 2, 
        # so we can divide p and q by 2 to reduce our equation.
        while p % 2 == 0 and q % 2 == 0:
            p, q = p / 2, q / 2

        # Eventually, only p or q will be even or both are odd.
        # If p is even then q is odd, and because s * p = r * q then r should be even
        if p % 2 == 0: 
            return 2   # numer of reflecting times is even means the ray ends at the top-left corner
        # If q is even then p is odd, and because s * p = r * q then s should be even
        elif q % 2 == 0: 
            return 0   # the number of stacked boxes is even means the current box is the flipped version of the original box so the top-right corner should be 0
        else: 
            return 1