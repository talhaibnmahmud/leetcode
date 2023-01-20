#include <string_view>
#include <unordered_map>


const std::unordered_map<char, uint16_t> roman_map = {
    {'I', 1},
    {'V', 5},
    {'X', 10},
    {'L', 50},
    {'C', 100},
    {'D', 500},
    {'M', 1000},
};

class Solution {
public:
    uint16_t romanToInt(std::string_view s) {
        uint16_t result = 0;

        for (auto i = 0; i < s.size(); ++i) {
            if (i + 1 < s.size() && roman_map.at(s[i]) < roman_map.at(s[i + 1])) 
                result -= roman_map.at(s[i]);
            else 
                result += roman_map.at(s[i]);
        }

        return result;
    }
};
