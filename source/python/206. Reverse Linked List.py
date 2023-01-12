# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next: ListNode | None = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return NotImplemented

        if other is None:
            return False

        return self.val == other.val and self.next == other.next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head

        current = head
        previous = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous


if __name__ == '__main__':
    solution = Solution()

    assert solution.reverseList(
        ListNode(
            1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
        )) == ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
                       )
    assert solution.reverseList(
        ListNode(1, ListNode(2))) == ListNode(2, ListNode(1))
    assert solution.reverseList(ListNode()) == ListNode()
    assert solution.reverseList(ListNode(1)) == ListNode(1)

    print("All tests passed!")
