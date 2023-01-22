#include <vector>


class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        if (nums.size() == 0) return 0;

        while (true) {
            auto it = std::find(nums.begin(), nums.end(), val);
            if (it == nums.end()) break;
            nums.erase(it);
        }

        return nums.size();
    }
};
