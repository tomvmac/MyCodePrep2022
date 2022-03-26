# Problem:
#
# Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:
#
# [] is worth 1 point
# XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
# [S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
# You may assume that the input only contains well-formed square brackets.


# Solution:
# 1. Use stack, init with 0 as point
# 2. Iterate through string
#    a. when you see open bracklet "[", push zero to the stack
#    b. when you see close bracklet "]", pop from the stack
#       i.  if number is a zero 0, add 1 point and push to the top of the stack
#       ii. if none zero, multiple it by 2 and push to the top of the stack


def nesting_score(string):
    stack = [0]

    for char in string:
        if char == '[':
            stack.append(0)
        else:
            popped = stack.pop()
            if popped == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2 * popped

    return stack[0]


print(nesting_score("[[][]][]")) # -> 5