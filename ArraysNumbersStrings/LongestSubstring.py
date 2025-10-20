# Given a string str made of alphabetical letters only,
# create a function that returns the length of the longest substring without repeating characters.

# Brute Force Solution
# 💡 Idea
#
# Generate all possible substrings.
#
# For each substring, check if all characters are unique.
#
# Keep track of the maximum length among those substrings.

# 🧩 Explanation
#
# Outer loop: start index of substring (i)
#
# Inner loop: end index of substring (j)
#
# set(substring) removes duplicates — if the size is unchanged, substring is unique.
#
# Compare and update max_length.

# ⏱️ Time Complexity
#
# There are O(n²) substrings.
#
# For each substring, checking uniqueness takes O(n).
#
# Total: O(n³)
#
# 💾 Space Complexity
#
# set(substring) can take up to O(n) space.
#
# Total: O(n)

def longest_unique_substring_bruteforce(s):
    max_length = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            # Check if all chars are unique
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))

    return max_length

print(longest_unique_substring_bruteforce("abcabcbb"))

# ⚡ Optimized Solution (Sliding Window + HashSet)
# 💡 Idea
#
# We can avoid re-checking substrings:
#
# Use two pointers (left, right) to define a sliding window.
#
# Use a set to store unique characters in the current window.
#
# Move right pointer to expand the window.
#
# If a duplicate appears, move left pointer until the duplicate is removed.

# ⏱️ Time Complexity
#
# Each character visited at most twice (once by right, once by left).
#
# O(n) total.
#
# 💾 Space Complexity
#
# The set can store up to all unique characters → O(n).

def longest_unique_substring_optimized(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # move right pointer until dups are found
        while s[right] in seen:
            # when dups appear, remove them from set and move left
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring_optimized("abcabcbb"))
