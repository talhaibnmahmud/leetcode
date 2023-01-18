class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        characters = [i for i in s if i.isalnum()]
        return characters == characters[::-1]


def test():
    s = Solution()

    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
