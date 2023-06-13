import math
from functools import lru_cache

# Function to calculate the number of divisors using memoization


@lru_cache(maxsize=None)
def calculate_divisors(n: int) -> int:
    div_count = 2  # Accounting for 1 and n as divisors

    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            div_count += 2  # Incrementing the count for two divisors: d and n/d

    # Check if n is a perfect square
    if math.isqrt(n) ** 2 == n:
        div_count -= 1  # Adjusting the count for a single divisor when n is a perfect square

    return div_count


# Read the values of a, b, and c
a, b, c = map(int, input().split())

# Initialize the result
result = 0

# Iterate through each value of i from 1 to a
for i in range(1, a + 1):
    # Iterate through each value of j from 1 to b
    for j in range(1, b + 1):
        # Calculate the product x
        x = i * j

        # Iterate through each value of k from 1 to c
        for k in range(1, c + 1):
            # Calculate the product y
            y = x * k

            # Calculate the number of divisors of y using memoization
            div_count = calculate_divisors(y)

            # Add div_count to the result
            result += div_count

# Print the result modulo 1073741824 (2^30)
print(result % 1073741824)
