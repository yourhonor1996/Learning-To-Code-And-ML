class Node:
    pass


class BinarySearchTree(object):
    # class Node(object):
    #     def __init__(self, data) -> None:
    #         self.data = data
    pass

    def traverse_inline(self, results, root="default") -> list:
        if root == "default":
            root = self.root

        if root.is_leaf:
            results.append(root)
            return

        self.traverse_inline(results, root.left)
        results.append(root)
        self.traverse_inline(results, root.right)


def is_binaryseach(tree: BinarySearchTree):
    root = tree.root
    inline_traversal = []
    tree.traverse_inline(inline_traversal)

    for i in range(1, len(inline_traversal)):
        if inline_traversal[i] < inline_traversal[i - 1]:
            return False
    return True
