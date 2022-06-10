# solution by Rui Wang
# problem description link: https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first, sort all strings in the list such that anagrams become the same.
        # fortunately the indices will be the same.
        sorted_strs = list(map(lambda a: str(sorted(a)), strs))
        
        # make a dictionary to record the indices of each anagram.
        sdict = {}
        for i in range(len(sorted_strs)):
            s = sorted_strs[i]
            if s not in sdict.keys():
                sdict[s] = []
            sdict[s].append(i)
        
        # for each word, take all the anagrams into the list.
        result = []
        for s in sdict.keys():
            lst = []
            for idx in sdict[s]:
                lst.append(strs[idx])
            result.append(lst)
        
        return result