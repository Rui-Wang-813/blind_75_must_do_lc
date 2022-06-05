# solution by Rui Wang
# problem description link: https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if target - num in numDict.keys():
                return [numDict[target - num], i]
            numDict[num] = i
        
        return []