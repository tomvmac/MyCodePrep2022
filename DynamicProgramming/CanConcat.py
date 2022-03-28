# Problem:
#
# Write a function, can_concat, that takes in a string and a list of words as arguments.
# The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.
#
# You may reuse words of the list as many times as needed.


# Solution:
# 1. Start with original string
# 2. Start to match the 1st char of the sentence with choices in word bank.None
#    a. if match, start removing/reducing that from the sentence
#    b. once no more matches, then it is a leaf or dead end
#
#
# Time:
# s = string length
# n = # of words
#
# O(n ^ s) - Brute Force
# O(n * s) - Memoization

def can_concat(s, words):
    return _can_concat(s, words, {})

def _can_concat(s, words, memo):
    if s in memo:
        return memo['s']

    if s == '':
        return True
        # Match 1st character with all words
    for word in words:
        # If match, remove char
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo) == True:
                memo[suffix] = True
                return memo[suffix]

    memo['s'] = False
    return False


print(can_concat("oneisnone", ["one", "none", "is"])) #  -> True
print(can_concat("oneisnone", ["on", "e", "is"])) #  -> False