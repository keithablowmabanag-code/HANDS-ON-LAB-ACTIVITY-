#MABANAG, KEITH ABLOW B.
#BSIT-2A
#LAB-3 HANDS ON
#DATA STRUCTURE AND ALGORITHM 

class Node:
    """A single node of a binary search tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree implemented from scratch."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert key into the BST; ignore duplicates."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        # Duplicates are ignored
        return node

    def search(self, key) -> bool:
        """Return True if key exists in the BST, otherwise False."""
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def _min_value_node(self, node):
        """Return the node with the smallest key in the given subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        """Delete key from the BST if present."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Case 1 & 2: zero or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children -> replace with inorder successor
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)

        return node

    def inorder(self) -> list:
        """Return keys in ascending order via inorder traversal."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.key)
        self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)
    print(bst.inorder())       # line A -> [20, 30, 35, 40, 45, 50, 60, 70, 80]
    print(bst.search(35))      # line B -> True
    print(bst.search(99))      # line C -> False
    bst.delete(20)             # leaf
    bst.delete(40)             # two children
    print(bst.inorder())       # line D -> [30, 35, 45, 50, 60, 70, 80]
