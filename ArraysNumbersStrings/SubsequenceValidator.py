# Problem:
#
# Given a sequence and an array, return whether the sequence is a subsequence of the array.
# A subsequence of an array is a set of numbers that aren't necessary adajent in the array,
# but are in the same orderas they appear in the array.

# Example:
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Solution:
# 1. Iterate through both array and sequence
# 2. When vals match, increment sequence counter
# 3. Otherwise, increment array counter
# 4. At the end, if the sequence has not been fully traversed then False

def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))