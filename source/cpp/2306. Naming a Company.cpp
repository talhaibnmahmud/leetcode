#include <string>
#include <unordered_set>
#include <vector>


class Solution {
public:
    long long distinctNames(std::vector<std::string>& ideas) {
        // Group idea by their initials.
        std::unordered_set<std::string> initialGroup[26];
        for (auto& idea : ideas)
            initialGroup[idea[0] - 'a'].insert(idea.substr(1));
        
        // Calculate number of valid names from every pair of groups.
        auto answer = 0LL;
        for (int i = 0; i < 25; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                // Get the number of mutual suffixes.
                int numOfMutual = 0;
                for (auto& ideaA : initialGroup[i]) {
                    if (initialGroup[j].count(ideaA))
                        numOfMutual++;
                }

                // Valid names are only from distinct suffixes in both groups.
                // Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                answer += (initialGroup[i].size() - numOfMutual) * (initialGroup[j].size() - numOfMutual) * 2;
            }
        }

        return answer;
    }
};
