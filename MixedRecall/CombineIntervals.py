# Problem:
#
# Write a function, combine_intervals, that takes in a list of intervals as an argument.
# Each interval is a tuple containing a pair of numbers representing a start and end time.
# Your function should combine overlapping intervals and return a list containing the combined intervals.

# Given two intervals:
#
# (1, 4) and (3, 7)
#
# The intervals overlap and
# should be combined into:
#
# (1, 7)

# Solution:
# 1. Sort Intervals
# 2. Init result interval list with 1st interval
# 3. Iterate through itervals (interval and compare to last element of result)
#    a. Check for overlap
#       i. if overlap, combine
#       ii. else, append to result

# Overlap meaning:
# ex) (1,4) (3, 7)
# last_start = 1
# last_end = 4
# current_start = 3
# current_end = 7




def combine_intervals(intervals):
    # sort the intervals
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    # Init combined with the first element of intervals
    combined = [sorted_intervals[0]]

    for current_interval in sorted_intervals[1:]:
        # get last element (start/end)
        last_start, last_end = combined[-1]
        # get current element (start/end)
        current_start, current_end = current_interval

        # Check for overlap
        if current_start <= last_end:
            if current_end > last_end:
                combined[-1] = (last_start, current_end)
        else:
            # no overlap, just append
            combined.append(current_interval)

    return combined


# intervals = [
#   (1, 4),
#   (12, 15),
#   (3, 7),
#   (8, 13),
# ]

intervals = [
  (3, 4),
  (2, 7),
    (4, 8)
]
print(combine_intervals(intervals))
# -> [ (1, 7), (8, 15) ]