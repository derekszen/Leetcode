# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # iterative solution
    # this solution is stupid.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode((l1.val + l2.val) % 10)
        if(l1.next is not None and l2.next is not None):
            temp1 = l1.next
            temp2 = l2.next
            if (l1.val + l2.val > 9):
                temp1.val += 1
            result.next = ListNode(temp1.val + temp2.val)
            resultptr = result.next
            temp1 = temp1.next
            temp2 = temp2.next
            while(temp1 is not None and temp2 is not None):
                if(temp1 is None):
                    temp1 = ListNode(0)
                elif(temp2 is None):
                    temp2 = ListNode(0)
                current = temp1.val + temp2.val
                if(current > 9):
                    
                resultptr.next = ListNode(current % 10)
                temp1 = temp1.next
                temp2 = temp2.next
        return result

    # recursive solution
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 is None and l2 is None):
            return result
        if(l1 is None):
            l1 = ListNode(0)
        elif(l2 is None):
            l2 = ListNode(0)
        nodeSum = l1.val + l2.val
        result = ListNode(nodeSum % 10)
        if(nodeSum > 9):
            if(l1.next is None):
                l1.next = ListNode(0)
            elif(l2.next is None): 
                l2.next = ListNode(0)
            l1.next.val += 1
            
        self.addTwoNumbers(l1.next, l2.next)
        self.addTwoNumbers(l1.next, l2.next)
