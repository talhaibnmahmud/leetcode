from typing import Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


def test():
    s = Solution()

    assert s.isSymmetric(None) == True
    assert s.isSymmetric(TreeNode(1)) == True
    assert s.isSymmetric(TreeNode(1, None, TreeNode(2))) == False
    assert s.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(2))) == True
    assert s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(
        4)), TreeNode(2, TreeNode(4), TreeNode(3)))) == True
    assert s.isSymmetric(TreeNode(1, TreeNode(
        2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))) == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
