# solution by Rui Wang
# problem description link: https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        # dp[i] represents how many ways are they to decode s[i:]
        dp = [0] * len(s)
        dp[-1] = 1 if s[-1] != '0' else 0
        if s[-2] == '0':
            dp[-2] = 0
        else:
            if int(s[-2:]) <= 26:
                # in thie case, assume s = '23', we have 2, 3 and 23.
                dp[-2] = dp[-1] + 1
            else:
                # in this case, assume s = '27, we have only 2, 7.
                dp[-2] = dp[-1]
        
        for i in range(len(s)-3, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            elif int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]

sol = Solution()
print(sol.numDecodings('12'))