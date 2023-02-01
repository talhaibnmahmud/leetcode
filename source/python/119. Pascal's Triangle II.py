class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]

        row = [1, 1]
        for i in range(2, rowIndex + 1):
            row = [1] + [row[j] + row[j + 1] for j in range(i - 1)] + [1]

        return row


def test():
    s = Solution()

    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1, 1]
    assert s.getRow(3) == [1, 3, 3, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
