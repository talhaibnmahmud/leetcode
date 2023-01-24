class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


def test():
    s = Solution()

    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
    assert s.lengthOfLastWord("a") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
