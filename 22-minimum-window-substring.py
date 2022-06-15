# solution by Rui Wang
# problem description link: https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) == 0:
            return ""
        
        # t_counter records the number of occurence of each unique char in t.
        # s_counter records the number of occurence of each unique char in s[lt:rt] that is also in t.
        t_counter = Counter(t)
        s_counter = {}
        
        # num_unique is the number of unique chars in t, and num_current is the number
        # of unique chars in s[lt:rt] that is also in t.
        num_unique = len(t_counter)
        num_current = 0
        
        lt_ptr, rt_ptr = 0, 0
        
        min_lptr, min_rptr = 0, 0
        
        while rt_ptr < len(s):
            c = s[rt_ptr]
            
            if c in t_counter.keys():
                if c not in s_counter.keys():
                    s_counter[c] = 0
                s_counter[c] += 1
                
                if s_counter[c] == t_counter[c]:
                    num_current += 1
                
                if num_current == num_unique:
                    
                    while lt_ptr <= rt_ptr:
                        lc = s[lt_ptr]
                        lt_ptr += 1

                        if lc in t_counter.keys():
                            s_counter[lc] -= 1
                            
                            if s_counter[lc] < t_counter[lc]:
                                num_current -= 1
                                break
                    
                    # now lt_ptr points to one char to the left of the starting point of current substr.
                    lt_ptr -= 1
                    if (min_lptr == 0 and min_rptr == 0) or (rt_ptr + 1 - lt_ptr) < (min_rptr - min_lptr):
                        min_lptr = lt_ptr
                        min_rptr = rt_ptr + 1
                    lt_ptr += 1
            
            rt_ptr += 1
        
        return s[min_lptr:min_rptr]

s = "ab"
t = "a"

sol = Solution()
print(sol.minWindow(s, t))