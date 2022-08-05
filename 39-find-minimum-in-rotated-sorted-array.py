# solution created by Rui Wang
# problem description link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        
        # find the index of the smallest element.
        def findK(lb, ub):
            if lb >= ub:
                return -1
            
            length = ub - lb
            midIdx = length // 2 - (0 if length % 2 else 1) + lb
            
            if nums[midIdx] < nums[-1]:
                if midIdx == 0 or (nums[midIdx - 1] > nums[midIdx]):
                    return midIdx
                return findK(lb, midIdx)
            
            return findK(midIdx + 1, ub)
        
        return nums[findK(0, len(nums))]