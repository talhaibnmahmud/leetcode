from typing import Self
from queue import Queue


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        queue: Queue[TreeNode] = Queue()
        queue.put(root)
        result: list[list[int]] = []

        while not queue.empty():
            level: list[int] = []
            for _ in range(queue.qsize()):
                node = queue.get()
                level.append(node.val)
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)
            result.append(level)

        return result


def test():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert Solution().levelOrder(None) == []
    assert Solution().levelOrder(TreeNode(1)) == [[1]]

    print("All tests passed!")


if __name__ == "__main__":
    test()
