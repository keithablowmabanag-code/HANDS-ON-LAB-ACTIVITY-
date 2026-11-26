#MABANAG, KEITH ABLOW B.
#BSIT-2A
#LAB-3 HANDS ON
#DATA STRUCTURE AND ALGORITHM 


from collections import deque


class Node:
    """A single node of a binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree identified by its root node."""

    def __init__(self, root_data):
        self.root = Node(root_data)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def build_tree():
    tree = BinaryTree(15)
    tree.root.left = Node(10)
    tree.root.right = Node(25)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(12)

    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(6)

    tree.root.right.left = Node(20)
    tree.root.right.right = Node(30)
    return tree.root


if __name__ == "__main__":
    root = build_tree()
    print("Inorder:", " ".join(map(str, inorder(root))))
    print("Preorder:", " ".join(map(str, preorder(root))))
    print("Postorder:", " ".join(map(str, postorder(root))))
    print("Level-order:", " ".join(map(str, level_order(root))))
