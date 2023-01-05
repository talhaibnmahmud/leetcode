# import itertools


class Solution:
    # # Most Naive Solution
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     all_comb = itertools.combinations(nums, 2)

    #     for pairs in all_comb:
    #         result = pairs[0] + pairs[1]

    #         if result == target:
    #             if pairs[0] != pairs[1]:
    #                 return [nums.index(pairs[0]), nums.index(pairs[1])]

    #             first = nums.index(pairs[0])
    #             second = nums.index(pairs[1], first + 1)
    #             return [first, second]

    #     return []

    # Efficient Solution using Hash Table
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}

        for index, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], index]

            hash_table[num] = index

        return []
