# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode()
        cur = new
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1: cur.next = l1
        else: cur.next = l2
        return new.next

# Method 2


# 特判：如果有一个链表为空，返回另一个链表
# 如果l1节点值比l2小，下一个节点应该是l1，应该return l1，在return之前，指定l1的下一个节点应该是l1.next和l2俩链表的合并后的头结点
# 如果l1节点值比l2大，下一个节点应该是l2，应该return l2，在return之前，指定l2的下一个节点应该是l1和l2.next俩链表的合并后的头结点


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2