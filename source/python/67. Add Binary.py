class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


def test():
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"

    print("All tests passed!")


if __name__ == "__main__":
    test()
