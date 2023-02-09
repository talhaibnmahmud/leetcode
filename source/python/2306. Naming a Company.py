class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        # Group the ideas by their first letter
        initial_groups: list[set[str]] = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord("a")].add(idea[1:])

        # Remove empty groups
        initial_groups = [group for group in initial_groups if group]

        answer = 0
        # Calculate the number of valid names from every pair of groups
        for i in range(len(initial_groups) - 1):
            for j in range(i + 1, len(initial_groups)):
                num_of_mutual = len(initial_groups[i] & initial_groups[j])

                # Valid names are only from distinct suffixes from both groups
                # Since we can a, b and b, a, we need to multiply by 2
                answer += (len(initial_groups[i]) - num_of_mutual) * \
                    (len(initial_groups[j]) - num_of_mutual) * 2

        return answer


def test():
    s = Solution()

    assert s.distinctNames(["coffee", "donuts", "time", "toffee"]) == 6
    assert s.distinctNames(["lack", "back"]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
