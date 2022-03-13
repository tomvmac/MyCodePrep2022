# Problem:
# Write a function, uncompress, that takes in a string as an argument.
# The input string will be formatted into multiple groups according to the given
# not pattern.

# For example:
# uncompress("2c3a1t") # -> 'ccaaat'
# uncompress("4s2b") # -> 'ssssbb'

# Solution:
# Strategy: Two Pointers

# Use two pointers i and j where i is used to keep track of numbers and j is used to track the char to be printed.


def uncompress(s):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j

    return ''.join(result)



# Driver

print(uncompress("2c3a1t"))