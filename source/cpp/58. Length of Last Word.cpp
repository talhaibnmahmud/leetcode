#include <cassert>
#include <iostream>
#include <string_view>



// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    int lengthOfLastWord(std::string_view s) {
        int length = 0;
        int end = s.size() - 1;

        while (end >= 0 && s[end] == ' ') end--;
        while (end >= 0 && s[end] != ' ') {
            length++;
            end--;
        }

        return length;
    }
};


int main()
{
    Solution solution;

    assertm(solution.lengthOfLastWord("Hello World") == 5, "Result is not 5");
    assertm(solution.lengthOfLastWord("   fly me   to   the moon  ") == 4, "Result is not 4");
    assertm(solution.lengthOfLastWord("luffy is still joyboy") == 6, "Result is not 6");
    assertm(solution.lengthOfLastWord("a") == 1, "Result is not 1");
    assertm(solution.lengthOfLastWord("a ") == 1, "Result is not 1");

    std::cout << "All tests passed." << std::endl;
}
