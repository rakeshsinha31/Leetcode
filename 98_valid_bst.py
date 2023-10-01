# Validate Binary Search Tree - Depth First Search - Leetcode 98
class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def is_valid_bst(self, Node):
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(Node, float("-inf"), float("inf"))


n = Node(val=5)
n.left = 1
n.right = 4
n.left.left = None
n.left.right = None
n.right.left = 3
n.right.right = 6
print(n.is_valid_bst(n))
