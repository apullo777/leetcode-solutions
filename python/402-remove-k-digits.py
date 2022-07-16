# https://leetcode.com/problems/remove-k-digits/

# Time: O(n)
# Speace: O(n)

class Solution:
    # preserve increasing sequence and remove decreasing sequence
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        # If no elements are removed, pop last elements, (increasing order)
        if k > 0:
            stack = stack[:-k]
        # removing leading zeros
        return "".join(stack).lstrip("0") or "0"