class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node_data, data):
        new_node = Node(data)
        pos = 0
        cur_node = self.head
        while cur_node:
            pos += 1
            cur_node = self.head.next
            if cur_node.data == prev_node_data:
                f_node = cur_node.next.next
                cur_node.next = new_node
                new_node.next = f_node
                break


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("1")
llist.insert("A", 2)
llist.print_list()
