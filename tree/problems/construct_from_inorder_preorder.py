preorder_dict = {}
inorder_dict = {}


class TNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.val = value


class Implementation:
    def __init__(self):
        pass

    # @staticmethod
    # def add_left(node: TNode, value: int):
    #     node.left = TNode(value)
    #
    # @staticmethod
    # def add_right(node: TNode, value: int):
    #     node.right = TNode(value)
    #
    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val)
        self.inorder_traversal(root.right)

    def construct(self, inorder, preorder, in_start, in_end, pre_start, pre_end):
        # print(in_start, in_end, pre_start, pre_end)
        if pre_start > pre_end or in_start > in_end:
            return None
        if pre_start == pre_end:
            node = TNode(preorder[pre_start])
            # print(node.val)
            return node
        node = TNode(preorder[pre_start])
        # print(node.val)
        in_index = inorder_dict[preorder[pre_start]]
        inl_start = in_start
        inl_end = in_index - 1
        inr_start = in_index + 1
        inr_end = in_end
        prel_start = pre_start + 1
        prel_end = prel_start + (inl_end - inl_start)
        prer_start = prel_end + 1
        prer_end = pre_end
        node.left = self.construct(inorder, preorder, inl_start, inl_end, prel_start, prel_end)
        node.right = self.construct(inorder, preorder, inr_start, inr_end, prer_start, prer_end)
        return node

    def build(self, inorder, preorder):
        for index, ele in enumerate(inorder):
            inorder_dict[ele] = index
        for index, ele in enumerate(preorder):
            preorder_dict[ele] = index
        root = TNode(preorder[0])
        # print(root.val)
        in_index = inorder_dict[preorder[0]]
        inl_start = 0
        inl_end = in_index - 1
        inr_start = in_index + 1
        inr_end = len(inorder) - 1
        prel_start = 1
        prel_end = prel_start + (inl_end - inl_start)
        prer_start = prel_end + 1
        prer_end = inr_end

        root.left = self.construct(inorder, preorder, inl_start, inl_end, prel_start, prel_end)
        root.right = self.construct(inorder, preorder, inr_start, inr_end, prer_start, prer_end)
        return root


tree = Implementation()
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
root = tree.build(inorder, preorder)
tree.inorder_traversal(root)
