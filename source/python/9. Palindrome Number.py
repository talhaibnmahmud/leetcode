class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     x = str(x)
    #     return x == x[::-1]

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        else:
            reverse = 0
            while x > reverse:
                reverse = reverse * 10 + x % 10
                x = x // 10
            if x == reverse or x == reverse // 10:
                return True
            else:
                return False


def test():
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
