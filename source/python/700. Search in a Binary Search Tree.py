from typing import Self


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


def test():
    s = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = s.searchBST(root, 2)
    assert result is not None and result.val == 2
    assert result.left is not None and result.left.val == 1
    assert result.right is not None and result.right.val == 3

    result = s.searchBST(root, 5)
    assert result is None

    print("All tests passed!")


if __name__ == "__main__":
    test()
