from queue import LifoQueue
from typing import Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def postorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     if root is None:
    #         return []

    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        stack: LifoQueue[TreeNode] = LifoQueue(maxsize=100)
        stack.put(root)

        result: list[int] = []

        while not stack.empty():
            node = stack.get()
            result.append(node.val)

            if node.left is not None:
                stack.put(node.left)
            if node.right is not None:
                stack.put(node.right)

        return result[::-1]


def test():
    s = Solution()
    assert s.postorderTraversal(
        TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [3, 2, 1]
    assert s.postorderTraversal(None) == []
    assert s.postorderTraversal(TreeNode(1)) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
