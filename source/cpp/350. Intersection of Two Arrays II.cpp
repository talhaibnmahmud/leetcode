#include <algorithm>
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
    // std::vector<int> intersect(std::vector<int>& nums1, std::vector<int>& nums2) {
    //     std::vector<int> result;

    //     std::sort(nums1.begin(), nums1.end());
    //     std::sort(nums2.begin(), nums2.end());

    //     int i = 0;
    //     int j = 0;

    //     while (i < nums1.size() && j < nums2.size()) {
    //         if (nums1[i] == nums2[j]) {
    //             result.push_back(nums1[i]);
    //             i++;
    //             j++;
    //         }
    //         else if (nums1[i] < nums2[j]) 
    //             i++;
            
    //         else 
    //             j++;
    //     }

    //     return result;
    // }

    std::vector<int> intersect(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::vector<int> result;
        std::unordered_map<int, int> temp;

        for (const auto& num : nums1) 
            temp[num]++;
        
        
        for (const auto& num : nums2) {
            if (temp.find(num) != temp.end() && temp[num] > 0) {
                result.push_back(num);
                temp[num]--;
            }
        }

        return result;
    }
};


int main()
{
    Solution solution;

    std::vector<int> nums1 = { 1, 2, 2, 1 };
    std::vector<int> nums2 = { 2, 2 };
    std::vector<int> result = solution.intersect(nums1, nums2);

    assertm(result == std::vector<int>({ 2, 2 }), "Result is not { 2, 2 }.");

    nums1 = { 4, 9, 5 };
    nums2 = { 9, 4, 9, 8, 4 };
    result = solution.intersect(nums1, nums2);

    assertm(result == std::vector<int>({ 4, 9 }) || result == std::vector<int>({ 9, 4 }), "Result is not { 4, 9 } or { 9, 4 }.");

    std::cout << "All tests passed." << std::endl;
}