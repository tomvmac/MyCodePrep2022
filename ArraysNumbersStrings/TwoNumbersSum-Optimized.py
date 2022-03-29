# Two Number Sum:
#
# Write a function that takes in a non-empty array of distinct integers and an integer representing
# a target sum. If any two numbers in the input array sum up to the target sum,
# the function should return them in an array, in any order.
#
# If no two numbers sum up to the target sum, the function should return an empty array.
#
#
# Sample Input:
#
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Time Complexity: o(n)
# Space Complexity: o(1)

def twoNumberSum(arr1, targetSum):
    sumArr = []

    # General Solution
    # Iterate through 1 loop

    # 1. init a hash table
    # 2. potentialMatch = targetSum - arr1[num1]
    # 3. if potentialMatch in hash table, return potentialMatch and arr1[num1]
    # 4. else add arr1[num1] to hash table


    # Iterate

    potentialMatch = 0
    numsHash = {}

    for num1 in range(len(arr1)):
        potentialMatch = targetSum - arr1[num1]
        if potentialMatch in numsHash:
            # add arr1[num1] and potentialMatch to sumArr and return
            sumArr.append(arr1[num1])
            sumArr.append(potentialMatch)
            return sumArr
        else:
            # add arr1[num1] to numsHash
            numsHash[arr1[num1]] = True
    return sumArr


arr1 = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

sumArr = twoNumberSum(arr1, targetSum)

print(sumArr)


