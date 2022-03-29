# Three Number Sum

# Write a function that takes in a non-empty array of distict integers and an integer representing a target sum.  The function should find all triplets
# in the array that sum up to the target sum and return a two dimensional array of all these triplets.  The numbers in each triplet should be ordered in
# ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

# If no three numbers sum up to the target sum, the function should return an empty array.


# General Strategy
# 1. Sort the array
# 2. Outer loop through the array
# 3. Inner loop use while and left and right pointers, loop until left pass or overlap right
#    a. sum = current + left + right
#    b. if sum == targetsum, add to triplets array, move both pointers, increment left, decrement right
#    c. if sum < targetsum, increment left
#    d. if sum > targetsum, decrement right

def threeNumberSum(array, targetSum):
    tripleArray = []

    array.sort()

    for i in range(len(array)-2):
        left = i + 1
        right = len(array)-1

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if  currentSum == targetSum:
                # if sum == targetsum, add to triplets array, move both pointers, increment left, decrement right
                tripleArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                # if sum < targetsum, increment left
                left += 1
            elif currentSum > targetSum:
                # if sum > targetsum, decrement right
                right -= 1

    return tripleArray



# Driver Code
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

expectedArray = [[-8,2,6], [-8,3,5], [-6,1,5]]
myArray = threeNumberSum(array, targetSum)

print("exepectedArray:", expectedArray)
print("myArray:", myArray)