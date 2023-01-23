#include <vector>


class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;

        while (right > left) {
            uint16_t mid = (left + right) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }

        if (nums[left] < target) return left + 1;
        return left;
    }
};
