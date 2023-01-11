#include <iostream>
#include <stack>
#include <string_view>


class Solution {
public:
    bool isValid(std::string_view s) {
        if (s.empty()) return true;
        if (s.size() % 2 != 0) return false;

        std::stack<char> stack;
        for (const auto& c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.empty()) return false;
                const auto top = stack.top();
                stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == ']' && top != '[') return false;
                if (c == '}' && top != '{') return false;
            }
        }

        return stack.empty();
    }
};
