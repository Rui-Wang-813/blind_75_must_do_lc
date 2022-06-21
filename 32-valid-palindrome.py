# solution by Rui Wang
# problem description link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        i, j = 0, len(s) - 1
        
        while i < j:
            # skip all chars that are not alphanumeric from both pointers.
            while i < j and not (s[i].isalpha() or s[i].isnumeric()):
                i += 1
            
            while j > i and not (s[j].isalpha() or s[j].isnumeric()):
                j -= 1
            
            if i == j:
                return True
            
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True