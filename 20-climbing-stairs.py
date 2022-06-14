# solution by Rui Wang
# problem description link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        
        dp[n] = 1
        dp[n-1] = 1
        
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]