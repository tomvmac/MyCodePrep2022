# basic loop


# simple for loop
arr1 = [1,2,3,4,5]
print ("-----------------------")
print("print array:")
for i in range(len(arr1)):
    print(arr1[i])

print(f"array size is {len(arr1)}")


# for each element loop - find element in array
def findItemInArray(arr, searchItem):
    for item in arr:
        if item == searchItem:
            return True
    return False

arr1 = [21,42,3,34,5]
print ("-----------------------")
print("findItemInArray:")
print(findItemInArray(arr1, 21))

