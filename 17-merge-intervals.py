# solution by Rui Wang
# problem description link: https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # firstly, sort by start of intervals.
        intervals.sort(key=lambda p: p[0])
        
        i = 0
        while i < len(intervals) - 1:
            a, b = intervals[i], intervals[i+1]
            
            if a[1] >= b[1]:
                # first interval covers second interval, simply remove second interval.
                intervals.remove(b)
            elif a[1] >= b[0] and a[1] < b[1]:
                # first interval ends at middle of second interval, simply expand first interval
                # and then remove second interval.
                a[1] = b[1]
                intervals.remove(b)
            else:
                # does not overlap.
                i += 1
        
        return intervals