from typing import Self
from queue import LifoQueue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     if root is None:
    #         return []

    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        stack: LifoQueue[TreeNode] = LifoQueue(maxsize=100)
        node = root
        result: list[int] = []

        while node is not None or not stack.empty():
            while node is not None:
                stack.put(node)
                node = node.left

            node = stack.get()
            result.append(node.val)
            node = node.right

        return result


def test():
    s = Solution()
    assert s.inorderTraversal(
        TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]
    assert s.inorderTraversal(None) == []
    assert s.inorderTraversal(TreeNode(1)) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
