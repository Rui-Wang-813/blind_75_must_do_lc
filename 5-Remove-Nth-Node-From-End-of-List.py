# solution by Rui Wang
# problem description link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# definition of singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use double pointer.

        # first pointer that precedes the second one by n number of nodes.
        t_head1 = head
        i = 0
        while i < n:
            t_head1 = t_head1.next
            i += 1
        
        # second pointer that points to the node before the node to be removed.
        t_head2 = head
        if t_head1 is None:
            # in this case, n == list size, so we remove the first node and return the second node.
            return t_head2.next
        
        # make sure the second pointer points to the node before the node to be removed.
        # by making the first pointer point to the last node.
        while t_head1.next != None:
            t_head1 = t_head1.next
            t_head2 = t_head2.next
        
        # remove this node.
        t_head2.next = t_head2.next.next
        
        # in other cases, head is always returned.
        return head