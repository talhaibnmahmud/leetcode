#include <vector>


class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        auto carry = 1;
        for (int i = digits.size() - 1; i > -1; --i) {
            digits[i] += carry;
            
            if (digits[i] > 9)
                digits[i] %= 10;
            else 
                return digits;
        }

        digits.insert(digits.begin(), 1);
        return digits;
    }
};