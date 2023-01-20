ROMAN = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for idx, char in enumerate(s):
            if idx < len(s) - 1 and ROMAN[char] < ROMAN[s[idx + 1]]:
                result -= ROMAN[char]
            else:
                result += ROMAN[char]

        return result


def test():
    solution = Solution()
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]
    for s, expected in test_cases:
        assert solution.romanToInt(
            s) == expected, f"{s=}, {expected=}, {solution.romanToInt(s)=}"

    print("All tests passed!")


if __name__ == "__main__":
    test()
