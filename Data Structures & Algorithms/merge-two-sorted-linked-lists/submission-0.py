# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        for head in (list1, list2):
            curr = head 
            while curr: 
                res.append(curr.val)
                curr = curr.next 
        res.sort()

        dummy = ListNode()
        tail = dummy 
        for v in res: 
            tail.next = ListNode(v)
            tail = tail.next 
        return dummy.next 
