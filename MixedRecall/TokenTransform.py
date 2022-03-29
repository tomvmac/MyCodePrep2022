# Problem:
#
# Write a function, token_transform, that takes in a dictionary of tokens and a string.
# In the dictionary, the replacement values for a token may reference other tokens.
# The function should return a new string where tokens are replaced with their fully evaluated string values.
#
# Tokens are enclosed in a pair of '$'.
#
# You may assume that their are no circular token dependencies.

# Solution

# 1. Identify as a graph, $A depends on $B in { $A$: 'This is $B$'}
# 2. DFS
# 3. DynamicProgramming to handle sub problems


def token_transform(s, token, memo):
    output = []
    i = 0
    j = 1

    while i < len(s):
        if s[i] != '$':
            output.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i:j + 1]
            value = token[key]
            if key in memo:
                evaluated_value = memo[key]
            else:
                evaluated_value = token_transform(value, tokens, memo)
            memo[key] = evaluated_value
            output.append(evaluated_value)
            i = j + 1
            j = i + 1
    return ''.join(output)


tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}



print(token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens, {}))
# -> 'Walk the dog in the dog park!