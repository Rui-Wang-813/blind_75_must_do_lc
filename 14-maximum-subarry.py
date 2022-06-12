# solution by Rui Wang
# problem description link: https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = nums[0]
        
        for i in range(1, len(nums)):
            if curSum < 0:
                maxSum = max(maxSum, curSum)
                curSum = nums[i]
            else:
                if nums[i] < 0:
                    maxSum = max(maxSum, curSum)
                curSum += nums[i]
        
        return max(maxSum, curSum)