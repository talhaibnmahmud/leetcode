from typing import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


def test():
    s = Solution()

    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = s.insertIntoBST(root, 5)
    assert result is not None and result.val == 4
    assert result.left is not None and result.left.val == 2
    assert result.left.left is not None and result.left.left.val == 1
    assert result.left.right is not None and result.left.right.val == 3
    assert result.right is not None and result.right.val == 7
    assert result.right.left is not None and result.right.left.val == 5

    root = TreeNode(
        40,
        TreeNode(20, TreeNode(10), TreeNode(30)),
        TreeNode(60, TreeNode(50), TreeNode(70))
    )
    result = s.insertIntoBST(root, 25)
    assert result is not None and result.val == 40
    assert result.left is not None and result.left.val == 20
    assert result.left.left is not None and result.left.left.val == 10
    assert result.left.right is not None and result.left.right.val == 30
    assert result.left.right.left is not None and result.left.right.left.val == 25
    assert result.right is not None and result.right.val == 60
    assert result.right.left is not None and result.right.left.val == 50
    assert result.right.right is not None and result.right.right.val == 70

    print("All tests passed!")


if __name__ == "__main__":
    test()
