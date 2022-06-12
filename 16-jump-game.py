# solution by Rui Wang
# problem description link: https://leetcode.com/problems/jump-game/

from typing import List

class Solution:

    # dp version, but too slow and exceeded time limit.
    def canJump_dp(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        # dp[i] is whether I can reach end from index i.
        dp = [False] * len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            n_steps = nums[i]
            
            for j in range(i+1, i+n_steps+1):
                if j >= len(nums):
                    break
                
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]
    
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        # max_pos records the maximum number of steps from index i that we can reach.
        # (not necessary from index i, maybe from some index before it)
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < 0:
                return False
            
            max_pos = max(nums[i], max_pos)
            max_pos -= 1
        
        return True