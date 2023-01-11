from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True

        if len(magazine) == 0 or len(ransomNote) > len(magazine):
            return False

        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)

        for key in ransomNote_counter:
            if key not in magazine_counter or ransomNote_counter[key] > magazine_counter[key]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()

    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True

    print("All tests passed!")
