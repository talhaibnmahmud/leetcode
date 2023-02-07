from collections import Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)

        basket: Counter[int] = Counter()
        max_count = 0
        count = 0

        start = 0
        for i in range(len(fruits)):
            basket[fruits[i]] += 1
            count += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
                count -= 1
            max_count = max(max_count, count)

        return max_count


def test():
    s = Solution()

    assert s.totalFruit([1, 2, 1]) == 3
    assert s.totalFruit([0, 1, 2, 2]) == 3
    assert s.totalFruit([1, 2, 3, 2, 2]) == 4
    assert s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test()
