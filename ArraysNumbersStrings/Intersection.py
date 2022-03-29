# Problem:
#
# Write a function, intersection, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are in both of the two lists.
#
# You may assume that each input list does not contain duplicate elements.

# Solution:
# 1. Loop through one list and add to map, pick the list with the smaller size
# 2. Loop through second list and check to see if it's in map, if so add to new list

def intersection(list1, list2):

    visitedMap = {}
    intersectionList = []

    if len(list1) > len(list2):
        visitedMap = createVisitedMap(list2)
        intersectionList = createIntersectionList(list1, visitedMap)
    else:
        visitedMap = createVisitedMap(list1)
        intersectionList = createIntersectionList(list2, visitedMap)

    return intersectionList

def createVisitedMap(list):
    visitedMap = {}

    for item in list:
        if item not in visitedMap:
            visitedMap[item] = 1

    return visitedMap


def createIntersectionList(list, visitedMap):
    intersectionList = []
    for item in list:
        if item in visitedMap:
            intersectionList.append(item)

    return intersectionList

# Driver Code
print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]

print(intersection([4,2,1], [1,2,4,6])) # -> [1,2,4]