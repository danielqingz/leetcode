# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# 输入：head = [1,3,2]
# 输出：[2,3,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Method 1 反转打印

class Solution:
    def reverse_print(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

# Method 2 递归

class Solution:
    def reverse_print(self, head):
        if not head: return []
        return self.reverse_print(head.next) + [head.val]

# Method 3 堆栈

class Solution:
    def reverse_print(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        res = []
        while stack:
            res.append(stack.pop(0))
        return res