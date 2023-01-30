from typing import Self
from queue import Queue


class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    #     def dfs(node: TreeNode | None, lower: int | float, upper: int | float) -> TreeNode | None:
    #         if not node:
    #             return None
    #         if node.val <= lower or node.val >= upper:
    #             return None
    #         if node.val == p.val or node.val == q.val:
    #             return node

    #         left = dfs(node.left, lower, node.val)
    #         right = dfs(node.right, node.val, upper)
    #         if left and right:
    #             return node
    #         return left or right

    #     return dfs(root, -math.inf, math.inf)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        queue: Queue[TreeNode] = Queue()
        queue.put(root)

        while not queue.empty():
            node = queue.get()
            if node.val > p.val and node.val > q.val and node.left:
                queue.put(node.left)
            elif node.val < p.val and node.val < q.val and node.right:
                queue.put(node.right)
            else:
                return node

        return None


def test():
    s = Solution()

    root = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9))
    )
    assert s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)) is root
    assert s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)) is root.left

    print("All tests passed!")


if __name__ == "__main__":
    test()
