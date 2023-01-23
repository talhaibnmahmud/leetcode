class Solution:
    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)

    #     for idx, num in enumerate(nums):
    #         if num > target:
    #             return idx

    #     return len(nums)

    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while high > low:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if nums[low] < target:
            return low + 1

        return low


def test():
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([1], 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
