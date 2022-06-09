# solution by Rui Wang
# problem description link: https://leetcode.com/problems/merge-k-sorted-lists/

from typing import Optional, List
from queue import PriorityQueue

# Definition for singly-linked list.
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
    
    # first version, merge lists one by one. This exceeded time limit.
    def mergeKLists_oneByOne(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        result = lists[0]
        
        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        
        return result
    
    # my own algo. Unfortunately this is too slow (only beat 5% python submissions).
    def mergeKLists_rui(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        result = ListNode()
        temp = result
        
        head_nodes = [node for node in lists if node != None]
        num_reach_end = k - len(head_nodes)
        
        while num_reach_end < k:
            idx = min(range(len(head_nodes)), key=lambda i: head_nodes[i].val)
            min_node = head_nodes[idx]
            
            temp.next = min_node
            temp = temp.next
            
            head_nodes[idx] = head_nodes[idx].next
            if head_nodes[idx] == None:
                head_nodes.pop(idx)
                num_reach_end += 1
        
        return result.next

    # this version uses priority queue. Also very slow. Also, we had to add a function to ListNode.
    def mergeKLists_queue(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(l)
        
        head = temp = ListNode()
        while not q.empty():
            node = q.get()
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                q.put(node)

        return head.next
    
    # this is the fastest version.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next