#include <array>
#include <cassert>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_map>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    // int firstUniqChar(std::string s) {
    //     if (s.empty()) return -1;

    //     std::unordered_map<char, int> map;
    //     for (const auto& c : s) 
    //         map[c]++;
        
    //     for (int i = 0; i < s.size(); i++) 
    //         if (map[s[i]] == 1) return i;
        
    //     return -1;
    // }


    int firstUniqChar(std::string_view s) {
        if (s.empty()) return -1;

        std::array<int, 26> arr = {0};
        for (const auto& c : s) 
            arr[c - 'a']++;
        
        for (int i = 0; i < s.size(); i++) 
            if (arr[s[i] - 'a'] == 1) return i;
        
        return -1;
    }
};


int main()
{
    Solution s = Solution();

    assertm(s.firstUniqChar("leetcode") == 0, "Assertion Failed: 'leetcode' -> 0");
    assertm(s.firstUniqChar("loveleetcode") == 2, "Assertion Failed: 'loveleetcode' -> 2");
    assertm(s.firstUniqChar("aabb") == -1, "Assertion Failed: 'aabb' -> -1");
    assertm(s.firstUniqChar("") == -1, "Assertion Failed: '' -> -1");

    std::cout << "All tests passed!" << std::endl;
}