# solution by Rui Wang
# problem description link: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        
        rt = 1

        curLen, maxLen = 1, 1
        while rt < len(nums):
            if nums[rt] == nums[rt-1] + 1:
                curLen += 1
            else:
                maxLen = max(maxLen, curLen)
                curLen = 1
            
            rt += 1
            # skip all duplicate elements.
            while rt < len(nums) and nums[rt] == nums[rt-1]:
                rt += 1
        
        # in case the last item is in the longest subsequence (maxLen not updated yet)
        return max(maxLen, curLen)

if __name__ == '__main__':
    lst = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()
    print(sol.longestConsecutive(lst))