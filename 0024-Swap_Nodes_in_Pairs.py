#1. iterative Time O(n), Space O(1) 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        node = dummyHead
        while node.next is not None and node.next.next is not None:           
            first = node.next                 # first = node.next 
            second = node.next.next           # second = first.next
            third = node.next.next.next       #
            node.next = second                # node.next = second
                                              # first.next = second.next
            node.next.next = first            # second.next = first   
            node = node.next.next             # node = first  
            node.next = third                 # 
        return dummyHead.next   
        
#1.5 answer, same as above except using head
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next
        
        
 #2. recursive Time O(n), Space O(n) 
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
