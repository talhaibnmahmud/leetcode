import math
from typing import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None, lower: int | float, upper: int | float) -> bool:
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -math.inf, math.inf)


def test():
    s = Solution()

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert s.isValidBST(root) is True
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert s.isValidBST(root) is False

    print("All tests passed!")


if __name__ == "__main__":
    test()
