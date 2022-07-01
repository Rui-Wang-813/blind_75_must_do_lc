# solution by Rui Wang
# problem description link: https://leetcode.com/problems/word-break/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        
        # dp[i] is whether s[i:] can be segmented.
        dp = [False] * (len(s)) + [True]
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i:i+len(word)]:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        
        return dp[0]