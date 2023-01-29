from queue import LifoQueue
from typing import Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def preorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     if root is None:
    #         return []
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        stack: LifoQueue[TreeNode] = LifoQueue(maxsize=100)
        stack.put(root)

        result: list[int] = []

        while not stack.empty():
            node = stack.get()
            result.append(node.val)

            if node.right is not None:
                stack.put(node.right)
            if node.left is not None:
                stack.put(node.left)

        return result


def test():
    s = Solution()
    assert s.preorderTraversal(
        TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 2, 3]
    assert s.preorderTraversal(None) == []
    assert s.preorderTraversal(TreeNode(1)) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
