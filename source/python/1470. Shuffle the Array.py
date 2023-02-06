class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result: list[int] = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        return result


def test():
    s = Solution()
    assert s.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert s.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test()
