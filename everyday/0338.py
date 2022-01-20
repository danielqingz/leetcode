# 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。

# 实现 Solution 类：

# Solution(ListNode head) 使用整数数组初始化对象。
# int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.arr)
