# solution by Rui Wang
# problem description link: https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        
        head1, head2 = list1, list2
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                temp.next = ListNode(val=head1.val)
                head1 = head1.next
            else:
                temp.next = ListNode(val=head2.val)
                head2 = head2.next
            temp = temp.next
        
        while head1 != None:
            temp.next = ListNode(head1.val)
            head1 = head1.next
            temp = temp.next
        
        while head2 != None:
            temp.next = ListNode(head2.val)
            head2 = head2.next
            temp = temp.next
        
        return result.next