# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        current = ListNode()
        carry = 0
        while (p is not None or q is not None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            carry = sum / 10
            current.next = ListNode(carry % 10)
            current = current.next
            if p.next is not None:
                p = p.next
            if q.next is not None:
                q = q.next

        if carry > 0:
            current.next = ListNode(carry)
        return current
