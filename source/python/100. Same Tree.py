# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' | None = None, right: 'TreeNode' | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution()

    assert solution.isSameTree(None, None) is True
    assert solution.isSameTree(None, TreeNode(1)) is False
    assert solution.isSameTree(TreeNode(1), None) is False

    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(3))) is True
    assert solution.isSameTree(TreeNode(1, TreeNode(
        2), None), TreeNode(1, None, TreeNode(2))) is False
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        1)), TreeNode(1, TreeNode(1), TreeNode(2))) is False

    print("All tests passed.")
