# Problem:
#
# Write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the strings are anagrams.
# Anagrams are strings that contain the same characters, but in any order.

# Solution:
# 1. Iterate through each list and store count per character in hash map
# 2. Iterate through one hash map, for each key find the count for the corresponding character, if any is not match count,
#     then false.
#
# Complexity Analysis:
# Time Complexity: O(n + m) - Iterate both lists
# Space Complexity: O(n + m) - Store both lists



def anagrams(s1, s2):
    s1Count = {}
    s2Count = {}

    for item in s1:
        if item not in s1Count:
            s1Count[item] = 0
        else:
            s1Count[item] += 1

    for item2 in s2:
        if item2 not in s2Count:
            s2Count[item2] = 0
        else:
            s2Count[item2] += 1


    # loop through first dict
    for key, value in s1Count.items():
        if not s2Count[key] or value != s2Count[key]:
            return False

    return True

    # return s1Count == s2Count



# Driver code
s1 = ['c','a','t','s']
s2 = ['t','s','c','d']

print(anagrams(s1, s2))