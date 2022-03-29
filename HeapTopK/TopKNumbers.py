from heapq import *

def find_k_largest_numbers_simple(nums, k):
  # Remember when using maxHeap, have to use - or negative numbers
  maxHeap = []
  topKNumbers = []

  # Iterate through nums and add to maxHeap
  for i in range(len(nums)):
    heappush(maxHeap, -nums[i])

  for i in range(k):
    topKNumbers.append(-heappop(maxHeap))

  return topKNumbers


def find_k_largest_numbers(nums, k):
  minHeap = []
  # put first 'K' numbers in the min heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # go through the remaining numbers of the array, if the number from the array is bigger than the
  # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers
  return minHeap



def main():
  print(find_k_largest_numbers_simple([3, 1, 5, 12, 2, 11], 3))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))


  # print("Here are the top K numbers: " +
  #       str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()