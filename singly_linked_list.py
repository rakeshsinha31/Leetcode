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
        """
        _Summary: Insert a new node after prev_node_data
        Args:
            prev_node_data: Data of the node after which the new is inserted
            data: Data of the new node to be inserted
        """
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

    def delete(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # if cur_node.next == None:
        #     return
        prev.next = cur_node.next
        cur_node = None

    def find_length(self):
        cur_node = self.head
        if cur_node.next is None:
            return 0

        length = 0
        while cur_node:
            cur_node = cur_node.next
            length += 1
        print(length)

    def swap_nodes(self, key1, key2):
        cur_node = self.head
        prev1 = None
        while cur_node:
            cur_node = cur_node.next
            if cur_node.data == key1:
                # prev1 =  cur_node
                node1 = cur_node
            if cur_node.data == key2:
                node2 = cur_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("1")
llist.insert("A", 2)
llist.print_list()
# llist.delete(2)
# llist.delete(1)
print("---------After deletion-----------")
llist.find_length()
