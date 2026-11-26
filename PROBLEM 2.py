#MABANAG, KEITH ABLOW B.
#DATA STRUCTURE AND ALGORITHM
#ACTIVITY 3
#PROBLEM 2

from collections import deque
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
# Build the same tree from Problem 1
root = Node(15)
root.left = Node(10)
root.right = Node(25)
 
root.left.left = Node(4)
root.left.right = Node(12)
 
root.right.left = Node(20)
root.right.right = Node(30)
 
root.left.left.left = Node(2)
root.left.left.right = Node(6)
 
 
def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)
 
 
def height(node):
    # Height uses the edges convention.
    # An empty tree has height -1.
    if node is None:
        return -1
 
    left_height = height(node.left)
    right_height = height(node.right)
 
    return 1 + max(left_height, right_height)
 
 
def iterative_size(root):
    if root is None:
        return 0
 
    queue = deque([root])
    count = 0
 
    while queue:
        node = queue.popleft()
        count += 1
 
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
 
    return count
 
 
print("Size:", size(root))
print("Height:", height(root))
print("Iterative size:", iterative_size(root))