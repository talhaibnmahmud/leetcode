#include <array>
#include <string_view>
#include <vector>


class Solution {
public:
    std::vector<int> findAnagrams(std::string_view s, std::string_view p) {
        if (s.size() < p.size()) return {};
        
        std::array<int, 26> pCount{};
        for (const auto& c : p)
            pCount[c - 'a']++;
        
        std::array<int, 26> sCount{};
        for (size_t i = 0; i < p.size(); i++)
            sCount[s[i] - 'a']++;
        
        std::vector<int> result;
        if (sCount == pCount)
            result.push_back(0);
        
        for (size_t i = p.size(); i < s.size(); i++) {
            sCount[s[i - p.size()] - 'a']--;
            sCount[s[i] - 'a']++;
            if (sCount == pCount)
                result.push_back(i - p.size() + 1);
        }

        return result;
    }
};
