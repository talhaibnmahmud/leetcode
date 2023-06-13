"""
The time complexity of this solution is O(T), where T is the number of test cases. We process each test case individually and perform constant time operations, so the overall time complexity is linear in the number of test cases.
"""

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the weight of pulp for the current test case
    N = int(input())

    # Calculate the number of notebooks that can be made
    notebooks = (N * 1000) // 100

    # Print the result
    print(notebooks)
