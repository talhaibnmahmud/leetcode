class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        currentMax = nums[0]

        for num in nums[1:]:
            currentMax = max(currentMax + num, num)
            ans = max(ans, currentMax)

        return ans
