# Problem:
#
# Write a function, token_replace, that takes in a dictionary of tokens and a string.
# The function should return a new string where tokens are replaced.
#
# Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted.
# Tokens should be replaced from left to right in the string (see test_05).


# Solution:
# 1. Use 2 pointers (i & j), init i = 0 and j = i + 1
# 2. Iterate right util i = '$', then iterate j until it reaches '$'
# 3. Grab the slice between i and j and that is the token, look up the token in dictionary
# 4. Replace with token value
# 5. Reposition i and j , i = j, j = i + 1

def token_replace(s, tokens):
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
            key = s[i: j + 1]
            output.append(tokens[key])
            i = j + 1
            j = i + 1

    return ''.join(output)


tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
# -> 'Walk the dog in the park!'