class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
# G = TreeNode(14)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
# D.left = G

# // pre_order = node->left->right
# // in_order = left->node->right
# // post_order = left->right->node

def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

def iterative_traversal(node):
    if not node:
        return
    
    stk = [node]
    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)



print("PRE ORDER")
pre_order(A)
print("IN ORDER")
in_order(A)
print("POST ORDER")
post_order(A)
print("Iterative traversal")
iterative_traversal(A)


