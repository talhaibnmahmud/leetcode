#include <iostream>
#include <string>
#include <string_view>


class Solution {
public:
    bool canConstruct(std::string_view ransomNote, std::string_view magazine) {
        if (ransomNote.empty()) return true;
        if (magazine.empty() || ransomNote.size() > magazine.size()) return false;

        int count[26] = { 0 };
        for (const auto& c : magazine) 
            count[c - 'a']++;
        
        for (const auto& c : ransomNote) {
            if (count[c - 'a'] == 0) return false;
            count[c - 'a']--;
        }

        return true;
    }
};