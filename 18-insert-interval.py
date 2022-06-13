# solution by Rui Wang
# problem description link: https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    # use binary search to find the index at which the new interval should be inserted.
    def binary_search(self, intervals, new_interval):
        if len(intervals) == 0:
            # actually, I should never get into this case.
            return 0
        if new_interval[0] <= intervals[0][0]:
            # in this case, insert at the beginning of list.
            return 0
        if new_interval[0] >= intervals[-1][0]:
            # in this case, insert at the end of the list.
            return len(intervals)
        
        n = len(intervals)
        mid = n // 2
        
        # find where I should insert this new interval in the left part.
        lt_idx = self.binary_search(intervals[:mid], new_interval)
        if lt_idx < mid:
            # in this case, the new interval might be inserted somewhere in the right half.
            return lt_idx
        
        # simply insert in the right half, and the index should be added with mid.
        rt_idx = self.binary_search(intervals[mid:], new_interval)
        return rt_idx + mid
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = self.binary_search(intervals, newInterval)    # first, find the index to insert.

        # then, simply insert.
        intervals = intervals[:idx] + [newInterval] + intervals[idx:]

        # since we are assured that there are no overlapping intervals in original list, we only need
        # to consider the index just before the new interval and the index right after index.
        i = max(0, idx - 1)
        while i < len(intervals) - 1 and i < idx + 1:
            a, b = intervals[i], intervals[i+1]

            if a[1] < b[0]:
                i += 1
            elif a [1] <= b[1]:
                a[1] = b[1]
                intervals.remove(b)
            else:
                intervals.remove(b)
        
        return intervals

intervals = [[1,4], [5,7], [9, 12], [17, 20]]
new_interval = [6, 8]

sol = Solution()
print(sol.insert(intervals, new_interval))