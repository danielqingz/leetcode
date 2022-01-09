class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if index >= self.size() or index < 0:
            print("Index error.")
            exit()
        cur_node = self.head
        while index > 0:
            cur_node = cur_node.next
            index -= 1
        return cur_node.data

    def size(self):
        if self.head is None:
            return 0
        position = 1
        cur_node = self.head
        while cur_node.next:
            position += 1
            cur_node = cur_node.next
        return position

# Build linked list

list1 = SLinkedList()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

list1.head = e1
list1.head.next = e2
e2.next = e3

print(e1.data, e1.next.data, e1.next.next.data, e1.next.next.next)
print(list1.get(2))

# Insert linked list, running time: O(1)

e4 = Node(4)
e2.next = e4
e4.next = e3

print(list1.get(1), list1.get(2), list1.get(3))

# Delete linked list, running time: O(n)

e2.next = e3
e4.next = None

