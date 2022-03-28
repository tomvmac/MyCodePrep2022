# Problem:
#
# Write a function, array_stepper, that takes in a list of numbers as an argument. You start at the first position of the list.
# The function should return a boolean indicating whether or not it is possible to reach the last position of the list.
# When situated at some position of the list, you may take a maximum number of steps based on the number at that position.

# Solution:
# 1. Loop through list
# 2. For each item, look at the value of the current index:
#    a. look at up to the value of positions to the right of the current value
#    b. track true/false for each


def array_stepper(numbers):
    return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(numbers) - 1:
        return True

    # For each iteration, get the max number of steps from value of the current index
    max_step = numbers[i]

    # Loop through all the possible steps
    for step in range(1, max_step + 1):
        # pass in the next step recursively
        if _array_stepper(numbers, step + i, memo) == True:
            memo[i] = True
            return memo[i]

    memo[i] = False
    return False
