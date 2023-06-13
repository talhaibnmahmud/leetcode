# Read the number of test cases
T = int(input())

# Iterate for each test case
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Calculate the total number of working hours in one week
    total_hours = (X * 4) + Y

    # Print the result
    print(total_hours)
