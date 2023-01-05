#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap{};

        for (int i = 0; i < nums.size(); i++)
        {
            if (hashmap.find(target - nums[i]) != hashmap.end())
            {
                return { hashmap[target - nums[i]], i };
            }

            hashmap[nums[i]] = i;
        }

        return {};
    }
};

int main()
{
    Solution solution;

    std::vector<int> nums{ 2, 7, 11, 15 };
    int target = 9;

    std::vector<int> result = solution.twoSum(nums, target);

    assertm(result.size() == 2, "Result size is not 2.");
    assertm(result[0] == 0, "Result[0] is not 0.");
    assertm(result[1] == 1, "Result[1] is not 1.");

    std::cout << "All tests passed." << std::endl;

    return 0;
}
