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
        # self.add_left(root.left.left.left, 50)
        self.add_left(root.left.right, 40)
        return root

    def balanced(self, root: TNode):
        if root is None:
            return True, 0
        lst = self.balanced(root.left)
        rst = self.balanced(root.right)
        if lst[0] and rst[0] and abs(lst[1] - rst[1]) <= 1:
            return True, (1 + max(lst[1], rst[1]))
        else:
            return False, 0

    def isBalanced(self, root: TNode):
        if self.balanced(root)[0]:
            return True
        else:
            return False


tree = Implementation()
root = tree.build()
print(tree.isBalanced(root))
