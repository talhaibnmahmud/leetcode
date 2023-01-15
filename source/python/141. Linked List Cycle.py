from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    val: int
    next: Self | None = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    # def __eq__(self, __o: object) -> bool:
    #     if not isinstance(__o, ListNode):
    #         return False

    #     return self.val == __o.val and self.next == __o.next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next                                # type: ignore
            fast = fast.next.next

        return True


def test():
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    # pos = 1
    assert head.next is not None and head.next.next is not None and head.next.next.next is not None
    head.next.next.next.next = head.next
    assert Solution().hasCycle(head) == True

    head = ListNode(1, ListNode(2))
    # pos = 0
    assert head.next is not None
    head.next.next = head
    assert Solution().hasCycle(head) == True

    head = ListNode(1)
    # pos = -1
    assert Solution().hasCycle(head) == False

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # pos = -1
    assert Solution().hasCycle(head) == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
