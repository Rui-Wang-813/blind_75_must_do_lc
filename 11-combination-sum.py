# solution by Rui Wang
# problem description: https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    # version 1.
    def combinationSum_ver1(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if len(candidates) == 0 or target < 0:
            return []
        
        result = []
        for i in range(len(candidates)):
            candidate = candidates[i]
            for comb in self.combinationSum_ver1(candidates[i:], target - candidate):
                result.append([candidate] + comb)
        
        return result
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def search(cand, target, stack):
            for i in range(len(cand)):
                if cand[i] > target:
                    return 
                if cand[i] == target:
                    result.append(stack + [cand[i]])
                    return 
                
                search(cand[i:], target - cand[i], stack + [cand[i]])
        
        search(candidates, target, [])
        return result

sol = Solution()
result = sol.combinationSum([2,3,6,7], 7)
print(result)