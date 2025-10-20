
# findDups
def findDups(arr):
    itemsVisited = {}
    for item in arr:
        if item not in itemsVisited:
            itemsVisited[item] = 1
        else:
            return item
    return None

print ("-----------------------")
print("findDups:")
print(findDups([4,5,7,8,4,9]))
print(findDups([4,5,7,8,1,9]))



