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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def search(self, key):
        if self.data > key:
            if not self.left:
                return False
            self.left.search(key)
        elif self.data < key:
            if not self.right:
                return False
            self.right.search(key)
        else:
            return True


tree = Node()
tree.insert(28)
tree.insert(36)
tree.insert(12)
tree.insert(14)
tree.insert(11)
tree.insert(16)
tree.insert(42)
tree.insert(30)
tree.insert(17)

tree.inorder()
print("---------------------")
tree.preorder()
print("---------------------")
tree.postorder()
print("---------------------")
tree.search(42)
