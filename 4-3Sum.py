# solution by Rui Wang
# problem description link: https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    # use dfs tree version and limited depth of 3, but time limit exceeded.
    def threeSum_rui(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(_nums, path):
            # returns when there are no more numbers in list or that depth had reached 3.
            if len(_nums) == 0 or len(path) == 3:
                return 
            
            i = 0
            while i < len(_nums):
                n = _nums[i]
                new_path = path + [n]
                # if we've reached the leaf, and that sum of the path is 0, append it to result.
                if len(new_path) == 3:
                    if sum(new_path) == 0:
                        result.append(new_path)
                # if we have not reached the leaf, go on.
                else:
                    dfs(_nums[i+1:], new_path)
                
                # make sure that the same number will not appear at this location ever again.
                i += 1
                while i < len(_nums) and _nums[i] == n:
                    i += 1
        
        # need to sort the nums so that there will be no duplicates.
        dfs(sorted(nums), [])
        return result
    
    # solution comes from https://www.code-recipe.com/post/three-sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list so that we can avoid duplicates.
        nums.sort()
        
        result = []
        
        i = 0
        while i < len(nums):
            # the target sum of the other two items.
            target = -nums[i]
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    # in this case we've found such triplets.
                    result.append([-target, nums[j], nums[k]])

                    # move the right pointer so that nums[k] is a different value.
                    # we do not need to worry about j now since it will be handled
                    # in following iterations.
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    # remember that nums is sorted.
                    j += 1
                else:
                    # remember that nums is sorted.
                    k -= 1
            
            # we've included all possible triplets starting with this number, so we do not
            # want this number to appear in the first position any more.
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        
        return result