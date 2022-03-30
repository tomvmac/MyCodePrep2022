def find_max_prod_brute(lst):
    # Time: O(^2)
    max_product = float('-inf')
    max_i = -1
    max_j = -1

    for i in lst:
        for j in lst:
            if max_product < i * j and i is not j:
                max_product = i * j
                max_i = i
                max_j = j

    return max_i, max_j


# Decimal library to assign infinite numbers
from decimal import Decimal


def find_max_prod(lst):
    # Multiply the minimum with the second minimum and the highest with the second highest
    # number of the list.Compare the products and then,
    # choose the numbers which give the higher product.

    # Time: O(n)

    max1 = lst[0]
    max2 = float('-inf')

    min1 = lst[0]
    min2 = float('inf')

    for number in lst:

        if number > max1:
            max2 = max1  # Second highest
            max1 = number  # First highest
        elif number > max2:
            max2 = number

        if number < min1:
            min2 = min1  # Second lowest
            min1 = number  # First lowest
        elif number < min2:
            min2 = number

    # Checking which pair has the highest product
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1




lst = [1, 3, 5, 2, 6]
num1, num2 = find_max_prod_brute(lst)
print(num1, num2)

num1, num2 = find_max_prod(lst)
print(num1, num2)
