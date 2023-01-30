import math
from typing import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        def dfs(node: TreeNode | None, lower: int | float, upper: int | float) -> bool:
            if not node:
                return False
            if node.val <= lower or node.val >= upper:
                return False
            if k - node.val in seen:
                return True

            seen.add(node.val)
            return dfs(node.left, lower, node.val) or dfs(node.right, node.val, upper)

        seen: set[int] = set()
        return dfs(root, -math.inf, math.inf)


def test():
    s = Solution()

    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2), TreeNode(4)),
        TreeNode(6, None, TreeNode(7))
    )
    assert s.findTarget(root, 9) is True
    assert s.findTarget(root, 28) is False

    print("All tests passed!")


if __name__ == "__main__":
    test()
