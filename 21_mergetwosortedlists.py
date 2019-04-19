# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# like the merge step of mergesort. 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        o1 = l1

        while(l1 is not None or l2 is not None):
            if(l1.val < l2.val):
                l1 = l1.next
            else:
                while(l1.next.val > l2.val):
                    t1 = l1.next
                    l1.next = l2
                else:
                    pass
            l2.next = 

        # add up remaining ones 
        while(l2 is not None):
            l1.next = l2
            l2 = l2.next

        # if l1 has remaining ones we are done anyways
        return o1
