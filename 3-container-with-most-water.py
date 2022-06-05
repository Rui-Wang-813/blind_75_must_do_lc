# solution by Rui Wang
# problem description link: https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = j * min(height[0], height[j])
        
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
        
        return max_area