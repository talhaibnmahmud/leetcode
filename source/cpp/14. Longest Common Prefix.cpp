#include <string>
#include <string_view>
#include <vector>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()) return "";

        std::string_view prefix = strs[0];
        for (const std::string_view str : strs) {
            while (str.find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.size() - 1);
                if (prefix.empty()) return "";
            }
        }

        return std::string(prefix);
    }
};