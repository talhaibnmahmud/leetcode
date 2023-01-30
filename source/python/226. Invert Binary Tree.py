from typing import Self
from queue import Queue


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def invertTree(self, root: TreeNode | None) -> TreeNode | None:
    #     if root is None:
    #         return None

    #     root.left, root.right = self.invertTree(
    #         root.right), self.invertTree(root.left)
    #     return root

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        queue: Queue[TreeNode] = Queue()
        queue.put(root)

        while not queue.empty():
            node = queue.get()
            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)

        return root


def test():
    s = Solution()

    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
                    )
    inverted = s.invertTree(root)
    assert inverted is not None and inverted.val == 4
    assert inverted.left is not None and inverted.left.val == 7
    assert inverted.right is not None and inverted.right.val == 2
    assert inverted.left.left is not None and inverted.left.left.val == 9
    assert inverted.left.right is not None and inverted.left.right.val == 6
    assert inverted.right.left is not None and inverted.right.left.val == 3
    assert inverted.right.right is not None and inverted.right.right.val == 1

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted = s.invertTree(root)
    assert inverted is not None and inverted.val == 2
    assert inverted.left is not None and inverted.left.val == 3
    assert inverted.right is not None and inverted.right.val == 1

    root = TreeNode(1)
    inverted = s.invertTree(root)
    assert inverted is not None and inverted.val == 1
    assert inverted.left is None
    assert inverted.right is None

    print("All tests passed!")


if __name__ == "__main__":
    test()
