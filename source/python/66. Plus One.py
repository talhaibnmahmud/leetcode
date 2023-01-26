class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)

        return digits


def test():
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([0]) == [1]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([9, 9]) == [1, 0, 0]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]

    print("All tests passed!")


if __name__ == "__main__":
    test()
