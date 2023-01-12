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
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        current = head
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == '__main__':
    solution = Solution()

    assert solution.deleteDuplicates(
        ListNode(1, ListNode(1, ListNode(2)))) == ListNode(1, ListNode(2))
    assert solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(
        2, ListNode(3, ListNode(3)))))) == ListNode(1, ListNode(2, ListNode(3)))

    print("All tests passed!")
