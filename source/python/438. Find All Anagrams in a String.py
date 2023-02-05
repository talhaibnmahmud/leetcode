from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        if (len(s) == len(p)) and (Counter(s) == Counter(p)):
            return [0]

        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        result: list[int] = []
        if s_counter == p_counter:
            result.append(0)

        for i in range(len(p), len(s)):
            s_counter[s[i]] += 1
            s_counter[s[i - len(p)]] -= 1
            if s_counter[s[i - len(p)]] == 0:
                del s_counter[s[i - len(p)]]

            if s_counter == p_counter:
                result.append(i - len(p) + 1)

        return result


def test():
    s = Solution()

    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test()
