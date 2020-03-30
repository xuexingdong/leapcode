# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        add_one = 0
        curr = ans
        while l1 or l1:
            value = 0
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            value += add_one
            mod = value % 10
            curr.next = ListNode(mod)
            curr = curr.next
            if value >= 10:
                add_one = 1
            else:
                add_one = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if add_one == 1:
            curr.next = ListNode(1)
        return ans.next
