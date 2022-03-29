# Problem:
#
# Write a function, most_frequent_char, that takes in a string as an argument.
# The function should return the most frequent character of the string.
# If there are ties, return the character that appears earlier in the string.
#
# You can assume that the input string is non-empty.


# Solution:
#
# 1. Break the string into characters
# 2. Add each character to a map, key is character and value is count
# 3. Iterate through string again and determine max count character


def most_frequent_char(s):
    charCount = {}
    maxCountChar = s[0]
    maxCount = 0

    for char in s:
        if char not in charCount:
            charCount[char] = 1
        else:
            charCount[char] += 1

    maxCount = charCount[maxCountChar]

    for char in s:
        if charCount[char] > maxCount:
            maxCount = charCount[char]
            maxCountChar = char

    return maxCountChar



# Driver Code
print(most_frequent_char('bookeeper'))
print(most_frequent_char('mississippi'))