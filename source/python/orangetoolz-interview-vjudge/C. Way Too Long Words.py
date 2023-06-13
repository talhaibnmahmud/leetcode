"""
The time complexity of this solution is O(n), where n is the number of words. This is because we iterate over each word once and perform constant time operations for each word. The overall time complexity is linear with respect to the number of words.
"""

# Read the number of words
n = int(input())

# Iterate for each word
for _ in range(n):
    # Read the word
    word = input()

    # Check if the word length is too long
    if len(word) > 10:
        # Create the abbreviation
        abbreviation = word[0] + str(len(word) - 2) + word[-1]

        # Print the abbreviation
        print(abbreviation)
    else:
        # Print the word as it is (not too long)
        print(word)
