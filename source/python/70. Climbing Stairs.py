class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev_step = 2
        before_prev_step = 1
        current = 0

        for _ in range(2, n):
            current = prev_step + before_prev_step
            before_prev_step = prev_step
            prev_step = current

        return current


def test():
    s = Solution()

    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test()
