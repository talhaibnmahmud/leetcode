class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


def test():
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
