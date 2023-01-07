#include <cassert>
#include <iostream>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int maxProfit = 0;
        int minPrice = INT_MAX;

        for (const auto& price : prices)
        {
            minPrice = std::min(minPrice, price);
            maxProfit = std::max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};


int main()
{
    Solution solution;

    std::vector<int> prices{ 7, 1, 5, 3, 6, 4 };
    int maxProfit = solution.maxProfit(prices);
    assertm(maxProfit == 5, "Max profit is not 5.");

    prices = { 7, 6, 4, 3, 1 };
    maxProfit = solution.maxProfit(prices);
    assertm(maxProfit == 0, "Max profit is not 0.");

    std::cout << "All tests passed." << std::endl;

    return 0;
}
