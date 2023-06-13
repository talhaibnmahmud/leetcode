# Read the number of test cases
T = int(input())

# Iterate for each test case
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Calculate the maximum number of people who can take a bath
    max_buckets = X // Y
    max_people = max_buckets // 2

    # Print the result
    print(max_people)
