# solution by Rui Wang
# problem description link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # special case
        if len(s) == 0:
            return 0
        
        # dp stores the length of longest substr ending in ith char.
        dp = [1] * len(s)
        # charDict stores the latest index of a char.
        charDict = {s[0]:0}
        for i in range(1, len(s)):
            c = s[i]
            # if this char never appeared the longest substr ending at it should just be the longest
            # substr ending at the char just before it, appending this last char.
            if c not in charDict.keys():
                dp[i] = dp[i-1] + 1
            else:
                # if the latest index of this char cannot be reached by the longest substr ending at
                # the char before this char, we do the same thing as the case above.
                if charDict[c] + dp[i-1] < i:
                    dp[i] = dp[i-1] + 1
                # otherwise, we are ensured that there are no other repeating chars between the last
                # appearance of this char and i, so just take dp[i] = i - charDict.
                else:
                    dp[i] = i - charDict[c]
            # update the lastest index of this char as i.
            charDict[c] = i
        
        return max(dp)