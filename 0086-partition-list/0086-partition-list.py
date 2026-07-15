# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        smaller = smaller_dummy
        greater = greater_dummy

        current = head

        while current:
            next_node = current.next
            current.next = None

            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                greater.next = current
                greater = greater.next

            current = next_node

        smaller.next = greater_dummy.next

        return smaller_dummy.next
        