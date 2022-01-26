# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# 方法1， 双指针cur，pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre