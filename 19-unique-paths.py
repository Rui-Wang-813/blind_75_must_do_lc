# solution by Rui Wang
# problem description link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m-1)]
        dp.append([1] * n)
        
        for i in range(m-1):
            dp[i][-1] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]