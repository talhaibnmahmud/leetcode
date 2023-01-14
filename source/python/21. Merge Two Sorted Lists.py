from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    val: int = 0
    next: Self | None = None

    def __str__(self):
        return f'{self.val} -> {self.next}'

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ListNode):
            return False

        return self.val == __o.val and self.next == __o.next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def test():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    expected = ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
    )
    assert Solution().mergeTwoLists(list1, list2) == expected

    list1 = None
    list2 = None
    expected = None
    assert Solution().mergeTwoLists(list1, list2) == expected

    list1 = None
    list2 = ListNode(0)
    expected = ListNode(0)
    assert Solution().mergeTwoLists(list1, list2) == expected

    print('All tests passed!')


if __name__ == '__main__':
    test()
