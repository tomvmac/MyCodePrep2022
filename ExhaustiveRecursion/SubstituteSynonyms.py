# Problem:
#
# Write a function, substituting_synonyms, that takes in a sentence and a dictionary as arguments.
# The dictionary contains words as keys whose values are arrays containing synonyms. The function should return an array containing
# all possible sentences that can be formed by substituting words of the sentence with their synonyms.
#
# You may return the possible sentences in any order, as long as you return all of them.


# Solution:
# 1. Split setence into list of words and conceptualize the combinations into a decision tree
# 2. For each level of the tree, we want to reduce the number of word by one
# 3. Each reduction can be a word:
#    a. not a synonym, in this case, we use the word
#    b. if synonym, further reduce

def substitute_synonyms(sentence, synonyms):
    words = sentence.split(' ')
    subarrays = generate(words, synonyms)
    return [' '.join(subarray) for subarray in subarrays]


def generate(words, synonyms):
    if len(words) == 0:
        return [[]]

    first_word = words[0]
    remaining_words = words[1:]

    subarrays = generate(remaining_words, synonyms)

    if first_word in synonyms:
        result = []
        for synonym in synonyms[first_word]:
            result += [[synonym, *subarray] for subarray in subarrays]
        return result
    else:
        return [[first_word, *subarray] for subarray in subarrays]


sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"]
}

print(substitute_synonyms(sentence, synonyms))
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]
