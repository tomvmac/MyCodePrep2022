# Problem:
#
# Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string.
# The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered
# according to the alphabet.
#
# You can assume that all characters are lowercase a-z.
#
# You can assume that the alphabet contains all 26 letters.
#
# Solution:
# 1. Iterate through words in wordlist
#     a. Compare two adjacent words
#     b. Use lexical order compare two words

def detect_dictionary(dictionary, alphabet):
    for i in range(0, len(dictionary)-1):
        if not lexical_order(dictionary[i], dictionary[i+1], alphabet):
            return False

    return True

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


dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"

print(detect_dictionary(dictionary, alphabet)) # -> True
