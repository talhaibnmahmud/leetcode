# import itertools
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if s1 == s2:
            return True

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True

        for i in range(len(s1), len(s2)):
            s2_counter[s2[i - len(s1)]] -= 1
            if s2_counter[s2[i - len(s1)]] == 0:
                del s2_counter[s2[i - len(s1)]]

            s2_counter[s2[i]] += 1

            if s1_counter == s2_counter:
                return True

        return False

    # Time limit exceeded
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False

    #     if s1 == s2:
    #         return True

    #     permutations = itertools.permutations(s1)
    #     for permutation in permutations:
    #         if "".join(permutation) in s2:
    #             return True

    #     return False


def test():
    s = Solution()

    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("adc", "dcda") == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
