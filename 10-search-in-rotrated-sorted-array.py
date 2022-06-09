# solution by Rui Wang
# problem description: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the pivot, and permute the list back.
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                break
            i += 1
        
        i += 1
        nums = nums[i:] + nums[:i]
        
        # perform binary search to find the target.
        n = len(nums)
        li, hi = 0, n - 1
        while li <= hi:
            mi = (li + hi) // 2
            if target > nums[mi]:
                li = mi + 1
            elif target < nums[mi]:
                hi = mi - 1
            else:
                return (mi + i) % n
        
        return -1