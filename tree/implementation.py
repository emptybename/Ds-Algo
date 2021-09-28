from collections import deque


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

    def preorder_traversal(self, root: TNode):
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self, root: TNode):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    def postorder_traversal(self, root: TNode):
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.val, end=" ")

    def iter_preorder_traversal(self, root: TNode):
        stack = deque()
        if root is None:
            return
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def iter_inorder_traversal(self, root: TNode):
        stack = deque()
        if root is None:
            return
        stack.append(root)
        root = root.left
        while stack or root is not None:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                print(node.val, end=" ")
                root = node.right

    def iter_postorder_traversal(self, root: TNode):
        if root is None:
            return
        stack1 = deque()
        stack2 = deque()
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().val, end=" ")

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


tree = Implementation()

root = tree.build()
tree.preorder_traversal(root)
print()
tree.iter_preorder_traversal(root)
print()
tree.inorder_traversal(root)
print()
tree.iter_inorder_traversal(root)
print()
tree.postorder_traversal(root)
print()
tree.iter_postorder_traversal(root)
print()
