# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null

# 哈希表

# 若头节点 head 为空节点，直接返回 nullnull ；
# 初始化： 哈希表 dic ， 节点 cur 指向头节点；
# 复制链表：
    # 建立新节点，并向 dic 添加键值对 (原 cur 节点, 新 cur 节点） ；
    # cur 遍历至原链表下一节点；
# 构建新链表的引用指向：
    # 构建新节点的 next 和 random 引用指向；
    # cur 遍历至原链表下一节点；
# 返回值： 新链表的头节点 dic[cur] ；

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]

