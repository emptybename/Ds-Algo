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
        return root

    def nodeCount(self, root: TNode):
        if root is None:
            return 0
        return 1 + self.nodeCount(root.left) + self.nodeCount(root.right)


tree = Implementation()
root = tree.build()
print(tree.nodeCount(root))
