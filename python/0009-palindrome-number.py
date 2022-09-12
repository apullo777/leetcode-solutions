# https://leetcode.com/problems/palindrome-number/

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# math: reverse the integer

class Solution:
    def isPalindrome(self, x: int) -> bool:
         # if x is negative, return False. 
         # if x is positive and last digit is 0, 
         # that also cannot form a palindrome, return False.
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        reverse, temp = 0, x
        while temp:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10
        return reverse == x

# instead of reversing the whole integer, 
# let's convert half of the integer and then check if it's palindrome.

# Example, if x = 15951, then let's create reverse of x in loop.
#  Initially, x = 15951, revX = 0

# x = 1595, revX = 1
# x = 159, revX = 15
# x = 15, revX = 159
# We see that revX > x after 3 loops 
# and we crossed the half way in the integer bcoz it's an odd length integer.
# If it's an even length integer, our loop stops exactly in the middle.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        reverse, temp = 0, x
        while temp > reverse:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10
        return (reverse == temp) or (temp == reverse // 10)