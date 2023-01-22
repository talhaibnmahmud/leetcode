class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break

        return len(nums)

    # def removeElement(self, nums: list[int], val: int) -> int:
    #     if not nums:
    #         return 0

    #     insert_index = 0
    #     for item in nums:
    #         if item != val:
    #             nums[insert_index] = item
    #             insert_index += 1

    #     return insert_index


def test():
    s = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert s.removeElement(nums, val) == 5

    nums = [3, 2, 2, 3]
    val = 3
    assert s.removeElement(nums, val) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
