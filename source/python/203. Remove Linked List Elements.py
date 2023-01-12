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
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None

        while head is not None and head.val == val:
            head = head.next

        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == '__main__':
    solution = Solution()

    assert solution.removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(
        5, ListNode(6))))))), 6) == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert solution.removeElements(None, 1) == None
    assert solution.removeElements(
        ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7) == None

    print("All tests passed!")
