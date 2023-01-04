#include <cassert>
#include <iostream>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    // Kadane's algorithm
    // Takes O(n) time
    int maxSubArray(std::vector<int>& nums) {
        int32_t ans = INT32_MIN;
        int32_t currentMax = 0;

        for (auto num : nums) {
            currentMax = std::max(num, currentMax + num);
            ans = std::max(ans, currentMax);
        }

        return ans;
    }

    // Does not work for all cases
    // Takes O(n^2) time
    // int maxSubArray(std::vector<int>& nums) {
    //     size_t n = nums.size();
    //     int32_t ans = INT32_MIN;

    //     for (size_t i = 0; i < n; i++) {
    //         int32_t sum = 0;
    //         for (size_t j = i; j < n; j++) {
    //             sum += nums[j];
    //             ans = std::max(ans, sum);
    //         }
    //     }

    //     return ans;
    // }
};


int main() {
    Solution solution;

    std::vector<int> case1 = { -2,1,-3,4,-1,2,1,-5,4 };
    assertm(solution.maxSubArray(case1) == 6, "Case 1 failed");
    std::cout << solution.maxSubArray(case1) << std::endl;

    std::vector<int> case2 = { 1 };
    assertm(solution.maxSubArray(case2) == 1, "Case 2 failed");
    std::cout << solution.maxSubArray(case2) << std::endl;

    std::vector<int> case3 = { 5,4,-1,7,8 };
    assertm(solution.maxSubArray(case3) == 23, "Case 3 failed");
    std::cout << solution.maxSubArray(case3) << std::endl;

    return EXIT_SUCCESS;
}