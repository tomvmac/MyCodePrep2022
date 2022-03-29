from heapq import *

def sum_of_elements_between_k1_k2(nums, k1, k2):
    minHeap = []
    sum = 0

    # Iterate through nums and push into minHeap
    for i in range(len(nums)):
        heappush(minHeap, nums[i])


    for i in range(k2-1):
        currentPop = heappop(minHeap)

        if i+1 > k1:
            sum += currentPop

    return sum



nums = [1, 3, 12, 5, 15, 11]
print(sum_of_elements_between_k1_k2(nums, 3, 6))