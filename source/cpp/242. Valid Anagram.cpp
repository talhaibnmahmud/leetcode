#include <iostream>
#include <string_view>


class Solution {
public:
    bool isAnagram(std::string_view s, std::string_view t) {
        if (s.size() != t.size()) return false;

        int count[26] = { 0 };

        for (const auto& c : s) count[c - 'a']++;
        for (const auto& c : t) {
            if (count[c - 'a'] == 0) return false;
            count[c - 'a']--;
        }

        return true;
    }
};