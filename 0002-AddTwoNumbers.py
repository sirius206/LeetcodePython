class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) 
        curr = dummy
        carry = 0
        x = 0
        y = 0
        while l1 or l2:
            if (l1):
                x = l1.val
            else:
                x = 0
            if (l2):
                y = l2.val
            else:
                y = 0         
            value = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            curr.next = ListNode(value)
            if (l1): l1= l1.next
            if (l2): l2 = l2.next
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(1, None)        
        return dummy.next    
