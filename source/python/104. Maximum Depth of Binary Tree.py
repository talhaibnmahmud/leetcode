from typing import Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test():
    s = Solution()

    assert s.maxDepth(None) == 0
    assert s.maxDepth(TreeNode(1)) == 1
    assert s.maxDepth(TreeNode(1, None, TreeNode(2))) == 2
    assert s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(
        20, TreeNode(15), TreeNode(7)))) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
