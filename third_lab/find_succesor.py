class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


def in_order_traversal(root):
    order_list = []
    current = root
    stack = []

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            order_list.append(current)
            current = current.right

    return order_list


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    value_list = in_order_traversal(tree)
    for i in range(len(value_list)-1):
        if value_list[i].value == node.value:
            return value_list[i+1]
    return None


root = BinaryTree(10)
root.left = BinaryTree(5, parent=root)
root.right = BinaryTree(15, parent=root)
root.left.left = BinaryTree(3, parent=root.left)
root.left.right = BinaryTree(7, parent=root.left)
root.right.right = BinaryTree(20, parent=root.right)
root.right.right.left = BinaryTree(12, parent=root.right.right)
print(find_successor(root, root.right.right.left))
