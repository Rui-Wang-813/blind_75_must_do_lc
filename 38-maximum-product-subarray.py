# solution by Rui Wang
# problem description link: https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = max(nums)
        
        # curMin is the min product ending at current element; curMax is the same.
        curMin, curMax = 1, 1
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            
            nextProd = curMax * num
            curMax = max(nextProd, curMin * num, num)
            curMin = min(nextProd, curMin * num, num)
            
            maxProd = max(curMax, maxProd)
            
        return maxProd

lst = [2, 3, -2, 4]

sol = Solution()
print(sol.maxProduct(lst))