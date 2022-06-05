# solution created by Rui Wang
# problem description link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # use stack structure and utilize its First-In-First-Out to solve this question.
        # stack process keeps the process recursively.
        stack = []
        
        i = 0
        while i < len(s):
            c = s[i]
            if c in '([{':
                # in this case, we simply push it onto stack.
                stack.insert(0, c)
            elif c not in ')]}':
                # what's this???
                return False
            else:
                # if the stack is empty, we know that this is a redundant
                # symbol, and thus return false.
                if len(stack) == 0:
                    return False
                
                pc = stack.pop(0)
                if '([{'.index(pc) != ')]}'.index(c):
                    # if this symbol is not correspondent to the top item of stack
                    # the order is wrong.
                    return False
            i += 1
        
        # there are unclosed paranthesis or not?
        return len(stack) == 0