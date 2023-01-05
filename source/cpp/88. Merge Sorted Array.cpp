#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    // void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
    //     for (size_t i = m; i < nums1.size(); i++)
    //         nums1[i] = nums2[i - m];
        
    //     std::sort(nums1.begin(), nums1.end());
    // }

    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j])
                nums1[k--] = nums1[i--];
            else
                nums1[k--] = nums2[j--];
        }
    }
};

int main()
{
    Solution s;
    std::vector<int> nums1 = { 1, 2, 3, 0, 0, 0 };
    std::vector<int> nums2 = { 2, 5, 6 };
    s.merge(nums1, 3, nums2, 3);
    assertm(nums1 == std::vector<int>({ 1, 2, 2, 3, 5, 6 }), "Test 1 failed");
    std::cout << "All tests passed!" << std::endl;
}