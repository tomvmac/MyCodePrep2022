# Problem:
#
# Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument.
# The function should return True if the first word should appear before the second word if
# lexically-ordered according to the given alphabet order. If the second word should appear first,
# then return False.
#
# Note that the alphabet string may be any arbitrary string.
#
# Intuitively, Lexical Order is like "dictionary" order:
#
# You can assume that all characters are lowercase a-z.
#
# You can assume that the alphabet contains all 26 letters.


# Notes:
# 1. Given an alphabet and two words or strings
# 2. Need to compare two words and see which one appears alphabetically first in the English dictionary

# Solution:
# 1. Iterate through both strings at corresponding indices
# 2. Iterate until chars are different from two strings
# 3. Check alphabet value for the given chars and compare
#    a. Take the one with less value first
#    b. If a char is missing, treat that as a very small char value
#
# Complexity:
# n = length of shorter word
#
# Time: O(n)

def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  # Iterate to the max of the two words
  for i in range(length):

    value_1 = float('-inf')
    value_2 = float('-inf')

    if i < len(word_1):
        value_1 = alphabet.index(word_1[i])

    if i < len(word_2):
        value_2 = alphabet.index((word_2[i]))


    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True



alphabet = "abcdefghijklmnopqrstuvwxyz"
print(lexical_order("apple", "dock", alphabet)) # -> True
print(lexical_order("apple", "app", alphabet)) # -> False
