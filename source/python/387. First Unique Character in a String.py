from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        count = Counter(s)

        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx

        return -1


if __name__ == '__main__':
    s = Solution()

    assert s.firstUniqChar("leetcode") == 0
    assert s.firstUniqChar("loveleetcode") == 2
    assert s.firstUniqChar("") == -1
    assert s.firstUniqChar("aabb") == -1

    print("All tests passed.")
