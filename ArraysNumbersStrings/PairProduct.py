# Problem:
#
# Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
#
# There is guaranteed to be one such pair whose product is the target.


# Solution:

# 1. Iterate through numbers, add current value as key and current index as value to hashmap
# if complement not found.
# 2. Otherwise return map value and current index as a dict

def pair_product(numbers, target_product):
  previous_nums = {}
  index = 0

  for num in numbers:
      complement = target_product / num
      if complement not in previous_nums:
          previous_nums[num] = index
          index += 1
      else:
          return (previous_nums[complement], index)

  return


# Driver Code
print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)

print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)