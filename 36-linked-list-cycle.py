# solution by Rui Wang
# problem description link: https://leetcode.com/problems/linked-list-cycle/

from utils import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1, ptr2 = head, head
        
        while ptr2 != None and ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
            if ptr2 == ptr1:
                return True
        
        return False