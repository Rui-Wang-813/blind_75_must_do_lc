# solution by Rui Wang
# problem description link: https://leetcode.com/problems/reorder-list/

from utils import ListNode, construct_LL_from_lst, print_LL
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use dictionary to map index to the ListNode.
        idx2Node = {}
        
        temp = head
        idx = 0
        while temp != None:
            idx2Node[idx] = temp
            temp = temp.next
            idx += 1
        
        # interleave the ListNode's.
        temp = ListNode()
        for i in range(idx // 2):
            temp.next = idx2Node[i]
            temp.next.next = idx2Node[idx - i - 1]
            
            temp = temp.next.next
        
        if idx % 2:
            temp.next = idx2Node[idx // 2]
            temp = temp.next
        temp.next = None

head = construct_LL_from_lst([1,2,3,4,5])
print_LL(head)

sol = Solution()
sol.reorderList(head)
print_LL(head)