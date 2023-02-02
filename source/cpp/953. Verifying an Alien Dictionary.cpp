#include <array>
#include <string>
#include <string_view>
#include <vector>


class Solution {
private:
    bool isSorted(std::string_view word1, std::string_view word2, const std::array<int, 26>& orderMap) const {
        for (auto i = 0; i < std::min(word1.size(), word2.size()); ++i) {
            if (word1[i] == word2[i]) continue;

            return orderMap[word1[i] - 'a'] < orderMap[word2[i] - 'a'];
        }

        return word1.size() <= word2.size();
    }
public:
    bool isAlienSorted(std::vector<std::string>& words, std::string_view order) const {
        std::array<int, 26> orderMap;
        for (auto i = 0; i < order.size(); ++i)
            orderMap[order[i] - 'a'] = i;

        for (int i = 0; i < words.size() - 1; ++i) {
            if (isSorted(words[i], words[i + 1], orderMap)) continue;
            
            return false;
        }

        return true;
    }
};
