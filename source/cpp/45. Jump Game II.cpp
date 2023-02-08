#include <vector>


class Solution {
public:
    int jump(const std::vector<int>& nums) const {
        if (nums.size() == 1) return 0;

        auto jumps = 0;
        auto currentJumpEnd = 0;
        auto maxReach = nums[0];

        for (auto i = 0; i < nums.size() - 1; i++) {
            maxReach = std::max(maxReach, i + nums[i]);
            
            if (i == currentJumpEnd) {
                jumps++;
                currentJumpEnd = maxReach;
            }
        }

        return jumps;
    }
};
