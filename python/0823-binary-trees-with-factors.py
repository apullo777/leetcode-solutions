# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # sorting makes sure that we only check values that are lesser than the current value 
        arr.sort()  
        mod = 10 ** 9 + 7
        
        dp = {}
        for num in arr:
            dp[num] = 1
            
        # loop through each number    
        for i, num in enumerate(arr):
            for j in range(i):
                if not (num % arr[j]) and (num // arr[j]) in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]] 
                    dp[num] %= mod
        return sum(dp.values()) % mod