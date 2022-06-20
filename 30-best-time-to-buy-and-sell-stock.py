# solution by Rui Wang
# problem description link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            # in this case, one can only buy stock and cannot earn anything.
            return 0
        
        maxSum = 0
        
        # two pointers.
        lt, rt = 0, 1
        while rt < len(prices):
            if prices[lt] < prices[rt]:
                maxSum = max(maxSum, prices[rt] - prices[lt])
            else:
                lt = rt
            
            rt += 1
        
        return maxSum