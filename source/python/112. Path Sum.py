from typing import Self
from queue import Queue


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        queue: Queue[TreeNode] = Queue()
        queue.put(root)

        while not queue.empty():
            node = queue.get()
            if node.left is None and node.right is None and node.val == targetSum:
                return True

            if node.left is not None:
                node.left.val += node.val
                queue.put(node.left)
            if node.right is not None:
                node.right.val += node.val
                queue.put(node.right)

        return False


def test():
    s = Solution()

    root = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    )
    assert s.hasPathSum(root, 22) == True

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.hasPathSum(root, 5) == False

    assert s.hasPathSum(None, 0) == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
