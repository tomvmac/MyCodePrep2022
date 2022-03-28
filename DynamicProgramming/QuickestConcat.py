# Problem:
#
# Write a function, quickest_concat, that takes in a string and a list of words as arguments.
# The function should return the minimum number of words needed to build the string by concatenating
# words of the list.
#
# You may use words of the list as many times as needed.

# Solution:
# 1. Start with original string
# 2. Start to match the 1st char of the sentence with choices in word bank.None
#    a. if match, start removing/reducing that from the sentence
#    b. once no more matches, then it is a leaf or dead end
# 3. Explore all combos and choose the minimum steps
#
# Time:
# s = string length
# n = # of words
#
# O(n ^ s) - Brute Force
# O(n * s) - Memoization

def quickest_concat(s, words):
    result = _quickest_concat(s, words, {})
    if result == float('inf'):
        return -1
    else:
        return result


def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]

    if s == '':
        return 0

    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            attempt = 1 + _quickest_concat(suffix, words, memo)
            min_words = min(attempt, min_words)

    memo[s] = min_words
    return min_words


print(quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond'])) # -> 4