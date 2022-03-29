# Problem:
#
# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example:
# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.


# Solution:
# 1. Create a map of num and its frequency
# 2. Push tuple of (frequency, num) to minHeap

from heapq import *

def find_k_frequent_numbers(nums, k):
    numFrequencyMap = {}
    minHeap = []
    results = []
    heapCount = 0

    # Iterate through nums, count and put in map
    for num in nums:
        if num not in numFrequencyMap:
            numFrequencyMap[num] = 1
        else:
            numFrequencyMap[num] += 1

    # Iterate through map and add to max heap
    for num, frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num))
        heapCount += 1

    for i in range(0, heapCount-k):
        heappop(minHeap)

    for i in range(0, k):
        frequency, num  = heappop(minHeap)
        results.append(num)

    return results

nums = [1, 3, 5, 12, 11, 12, 11]
k = 2
print(find_k_frequent_numbers(nums, k))




