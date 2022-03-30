# Problem:
#
# Product Sum contains an array that can contain a special array.
#
# A special array is a non-empty array that contains either integers or other special arrays
# The product sum of a special array is the sum of its elements, where special arrays inside are
# summed themselves and then multiplied by their level of depth
#


def product_sum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += product_sum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier


array = [5,2, [7 -1], 3, [6, [-13, 8],4]]
print(product_sum(array))