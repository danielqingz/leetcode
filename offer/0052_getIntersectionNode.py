# 输入两个链表，找出它们的第一个公共节点。

# Method 1 双指针

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next
            else: cur1 = headB

            if cur2:
                cur2 = cur2.next
            else: cur2 = headA
        return cur1