# Problem: Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
# https://leetcode.com/problems/missing-number/solution/


# Solution:
# 1. Get the sum of numbers, total = n * (n+1)/2
# 2. Subtract all the numbers from sum and you get missing number

def missingNumber(arr):
    sum = 0
    expectedSum = 0

    # loop through length of arr to get calculate sum.
    for i in range(1, len(arr)):
        expectedSum += 1

    print(expectedSum)


    return


arr1 = [1, 2, 3, 4, 5, 7, 8]
print(missingNumber(arr1))

