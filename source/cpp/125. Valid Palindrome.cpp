#include <string>
#include <string_view>


class Solution {
public:
    bool isPalindrome(std::string_view s) {
        if (s.empty()) return true;

        auto left = s.begin();
        auto right = s.end() - 1;
        while (left < right) {
            if (!std::isalnum(*left)) {
                ++left;
                continue;
            }
            if (!std::isalnum(*right)) {
                --right;
                continue;
            }
            if (std::tolower(*left) != std::tolower(*right)) {
                return false;
            }
            ++left;
            --right;
        }
        
        return true;
    }
};