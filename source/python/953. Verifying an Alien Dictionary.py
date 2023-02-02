class Solution:
    def compare(self, word1: str, word2: str, order_dict: dict[str, int]) -> bool:
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                continue

            return order_dict[word1[i]] < order_dict[word2[i]]

        return len(word1) <= len(word2)

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            if not self.compare(words[i], words[i + 1], order_dict):
                return False

        return True


def test():
    s = Solution()

    assert s.isAlienSorted(
        ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(
        ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False
    assert s.isAlienSorted(
        ["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
