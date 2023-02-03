class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        row = 0
        down = True

        for c in s:
            rows[row] += c
            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False

            row += 1 if down else -1

        return ''.join(rows)


def test():
    s = Solution()

    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("A", 1) == "A"

    print("All tests passed!")


if __name__ == "__main__":
    test()
