#include <unordered_map>
#include <vector>


class Solution {
public:
    int totalFruit(const std::vector<int>& fruits) const {
        if (fruits.size() < 3) return fruits.size();

        std::unordered_map<int, int> basket;
        auto maxFruits = 0;
        auto left = 0;

        for (auto right = 0; right < fruits.size(); right++) {
            basket[fruits[right]]++;

            while (basket.size() > 2) {
                if (--basket[fruits[left]] == 0)
                    basket.erase(fruits[left]);
                
                left++;
            }

            maxFruits = std::max(maxFruits, right - left + 1);
        }

        return maxFruits;
    }
};
