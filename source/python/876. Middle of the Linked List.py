from typing import Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next                # type: ignore (slow is not None)
            fast = fast.next.next

        return slow


def test():
    s = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    middle = s.middleNode(head)
    assert middle is not None and middle.val == 3

    head = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
    )
    middle = s.middleNode(head)
    assert middle is not None and middle.val == 4

    print("All tests passed!")


if __name__ == "__main__":
    test()
