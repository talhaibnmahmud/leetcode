#include <vector>


class Solution {
public:
    uint16_t removeDuplicates(std::vector<int>& nums) {
        if (nums.size() == 1) return 1;

        uint16_t insertIndex = 0;
        for (uint16_t i = 1; i < nums.size(); i++) {
            if (nums[insertIndex] != nums[i]) {
                insertIndex++;
                nums[insertIndex] = nums[i];
            }
        }

        return insertIndex + 1;
    }
};
