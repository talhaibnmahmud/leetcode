from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter


if __name__ == '__main__':
    s = Solution()

    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False

    print("All tests passed!")
