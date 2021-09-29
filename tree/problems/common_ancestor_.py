class TNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.val = value


class Implementation:
    def __init__(self):
        pass

    @staticmethod
    def add_left(node: TNode, value: int):
        node.left = TNode(value)

    @staticmethod
    def add_right(node: TNode, value: int):
        node.right = TNode(value)

    def build(self):
        root = TNode(10)
        self.add_left(root, 2)
        self.add_right(root, 3)
        self.add_left(root.left, 4)
        self.add_right(root.left, 5)
        self.add_left(root.right, 20)
        self.add_right(root.right, 8)
        self.add_left(root.left.left, 11)
        self.add_left(root.left.left.left, 50)
        self.add_left(root.left.right, 40)
        return root

    def find_common_ancestor(self, root: TNode, n1: TNode, n2: TNode):
        if root is None:
            return None
        if root == n1 or root == n2:
            return root
        lt = self.find_common_ancestor(root.left, n1, n2)
        rt = self.find_common_ancestor(root.right, n1, n2)
        if lt is not None and rt is not None:
            return root
        elif lt is not None:
            return lt
        else:
            return rt


tree = Implementation()
root = tree.build()
print(tree.find_common_ancestor(root, root.left, root.left.right).val)
