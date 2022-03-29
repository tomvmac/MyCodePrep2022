# Longest Peak

# Write a function that takes an array on integers and returns the length of the longest peak in the array.

# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
# (the highest value in the peak), at which point they become strictly decreasing.
# At least three integers are required to form a peak.

# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.

# Similarly, the integers 1, 2, 3 don't form a peak because they are strictly decreasing after the 3.

# General strategy
# 1. Loop (outer loop) - Find Peak
#    a. Compare num to left and right, if greater than both, then peak
#    b. While loop, move left and right until not descending, count peak length, compare and store as longestPeak if greater

def longestPeak(array):
    longestPeak = 0

    if len(array) < 3:
        return longestPeak

    # start with 2nd element and end at the
    curr = 1
    while curr < len(array)-1:
        currPeak = 0
        # peak check, peak is true when curr is greater than both left and right values
        if array[curr] > array[curr-1] and array[curr] > array[curr + 1]:
            # move left and right until stop descending and count
            left = curr - 1
            right = curr + 1
            hasMoreLeftItems = True
            hasMoreRightItems = True
            currPeak = 3

            if len(array) > 3:
                while hasMoreLeftItems or hasMoreRightItems:
                    if hasMoreLeftItems and left > 0:
                        if array[left] > array[left-1]:
                            currPeak += 1
                            left -= 1
                        else:
                            hasMoreLeftItems = False
                    else:
                        hasMoreLeftItems = False

                    if hasMoreRightItems and right <= len(array)-2:
                        if array[right] > array[right+1]:
                            currPeak += 1
                            right += 1
                        else:
                            hasMoreRightItems = False
                    else:
                        hasMoreRightItems = False


            if currPeak > longestPeak:
                longestPeak = currPeak

        curr += 1

    return longestPeak


# Driver Code

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# array = [1, 3, 2]
# array = [1, 2, 3, 4, 5, 1]
print(longestPeak(array))