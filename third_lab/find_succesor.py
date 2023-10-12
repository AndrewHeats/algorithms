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

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value, parent=self)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value, parent=self)
            else:
                self.right.insert(value)

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
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(20)
root.insert(12)
print(find_successor(root, BinaryTree(7)))
