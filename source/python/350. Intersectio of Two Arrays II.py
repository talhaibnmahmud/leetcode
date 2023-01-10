from collections import Counter


class Solution:
    # def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    #     nums1.sort()
    #     nums2.sort()

    #     i = 0
    #     j = 0
    #     result: list[int] = []

    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] == nums2[j]:
    #             result.append(nums1[i])
    #             i += 1
    #             j += 1
    #         elif nums1[i] < nums2[j]:
    #             i += 1
    #         else:
    #             j += 1
    #     return result

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = []
        temp = Counter(nums1)

        for num in nums2:
            if temp[num] > 0:
                result.append(num)
                temp[num] -= 1

        return result
