# Problem:
#
# Write a function, paired_parentheses, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
#
# You may assume the string contains only alphabetic characters, '(', or ')'.

# Solution:
# 1. Init a count
# 2. Increment count when there is an opener "("
# 3. Decrement count when there is a closer ")"
# 4. If count at the end is 0, then return True, else return False


def paired_parentheses(phrase):
    count = 0
    for char in phrase:
        if char == "(":
            count += 1
        if char == ")":
            if count == 0:
                return False
            else:
                count -= 1


    if count == 0:
        return True
    else:
        return False


# print(paired_parentheses("(david)((abby))")) # -> True
# print(paired_parentheses(")(")) # -> False
print(paired_parentheses("))()")) # False