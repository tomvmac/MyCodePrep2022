# Problem:

# Write a function, compress, that takes in a string as an argument.
# The function should return a compressed version of the string where consecutive occurrences of
# the same characters are compressed into the number of occurrences followed by the character.
# Single character occurrences should not be changed.

# Examples:
# compress('ccaaatsss') # -> '2c3at3s'


# Solution:
# Use two pointers, i and j.  Increment j on every step until next char is diff than the one at i position.  Then take the count as the difference
# between i and j and print the char at i.  Move i to j and continue.  The edge case is to insert an extra character to the initial string.
# so the comparison and append works as expect due to the end of the string will not have a different character.



def compress(s):
    s += "!"
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            result.append(str(j-i) + s[i])
            i = j

    return ''.join(result)


# Driver code
print(compress('ccaaatsss'))
