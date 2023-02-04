#include <array>
#include <ranges>
#include <string_view>


class Solution {
public:
    bool checkInclusion(std::string_view s1, std::string_view s2) {
        if (s1.size() > s2.size()) return false;
        if (s1 == s2) return true;

        std::array<int, 26> s1_count{};
        for (const auto& c : s1) {
            s1_count[c - 'a']++;
        }

        std::array<int, 26> s2_count{};
        for (size_t i = 0; i < s1.size(); i++)
            s2_count[s2[i] - 'a']++;
        
        if (s1_count == s2_count) return true;

        for (size_t i = s1.size(); i < s2.size(); i++) {
            s2_count[s2[i - s1.size()] - 'a']--;
            s2_count[s2[i] - 'a']++;
            if (s1_count == s2_count) return true;
        }

        return false;
    }
};