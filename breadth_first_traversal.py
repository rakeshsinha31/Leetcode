class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = Node(value)
        if not self.data:
            self.data = value
        else:
            if value < self.data:
                if not self.left:
                    self.left = new_node
                else:
                    self.left.insert(value)
            else:
                if not self.right:
                    self.right = new_node
                else:
                    self.right.insert(value)

    def bft(self):
        """
        BFT is also call level order traversal. Travel the each level,
        meaning travel a node and it's children at the same level then move to next level
        """
        que = []
        visited_node = []
        if not self.data:
            return que
        que.append(self.data)
        visited_node.append(self)
        # while len(visited_node) > 0:
        for each_node in visited_node:
            if each_node.left:
                que.append(each_node.left.data)
                visited_node.append(each_node.left)
            if each_node.right:
                que.append(each_node.right.data)
                visited_node.append(each_node.right)
        print(que)


tree = Node()
tree.insert(28)
tree.insert(36)
tree.insert(12)
tree.insert(14)
tree.insert(11)
tree.insert(42)
tree.insert(30)
tree.insert(45)
tree.insert(4)
tree.bft()
