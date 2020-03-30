# Problem

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Example

```text
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

# Solution

自然运算，注意进位以及首位为进位得到1的情况。

```python
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

```

时间复杂度`max(l1, l2)`，空间复杂度`max(l1, l2)`。