# 1. Two pass, first count, then remove count - n + 1th node
# Time O(L), Space O(1) 
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        dummyHead = ListNode(0)
        dummyHead.next = head
        node = dummyHead.next
        while node is not None:
            count += 1
            node = node.next
        remove = count - n + 1
        node = dummyHead
        prev = node
        for i in range(remove):
            prev = node
            node = node.next
        node = node.next    
        prev.next = node
        return dummyHead.next   
            
# 2. One pass, Two pointers, The first pointer advances the list by n+1n+1 steps from the beginning, 
# while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by nn nodes apart. 
# We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. 
# The second pointer will be pointing at the nnth node counting from the last. 
# Time O(L), Space O(1)      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        first = dummyHead
        second = dummyHead
        for i in range (n + 1):
            first = first.next
            
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummyHead.next   
            
