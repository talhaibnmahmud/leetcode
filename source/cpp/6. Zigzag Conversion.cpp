#include <numeric>
#include <string>
#include <string_view>
#include <vector>


class Solution {
public:
    std::string convert(std::string_view s, const int& numRows) const {
        if (numRows == 1) return std::string(s);

        std::vector<std::string> rows(numRows);
        auto row = 0;
        bool down = true;

        for (const auto& c : s) {
            rows[row] += c;
            
            if (row == 0) down = true;
            else if (row == numRows - 1) down = false;

            row += down ? 1 : -1;
        }

        return std::accumulate(rows.begin(), rows.end(), std::string());
    }
};