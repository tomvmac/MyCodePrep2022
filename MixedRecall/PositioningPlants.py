# Problem:
#
# You've been hired to plant flowers in a garden with n different positions. There are m different flower types.
# The prices of flowers types vary depending on which position they are planted.
# Your bosses are picky, they tell you to never plant two of the same flower type right next to each other.
# What is the minimum cost we need to plant a flower in each position of the garden?
#
# Write a function, positioningPlants, that takes in a 2D list with dimensions n * m.
# Each row of the list represents the costs of the flower types at that position.
# This means that costs[i][j] represents the cost of planting flower type j at position i.
#
# For example:
#
# Given these costs,
#
# costs = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]
#
# The costs of plants at position 1 are $6, $1, and $9.
# The cost of planting flower type 0 at position 1 is $6.
# The cost of planting flower type 2 at position 1 is $9.

# Notes:
# 1. Need to track pos, last_plant
# 2. Create a decision tree
# 3. From root to leaf, find the least cost
# 4. Leaf is 0
# 5. Bubble up, add node value to edge and then choose min value

# costs = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]

# Solution
# 1. Tree with values of pos, last_plant

# Complexity:
# n = # positions
# m = # plant types
#
# Time: O(m ^n) for brute, O(nm) for memo
# Space: O(n)

def positioning_plants(costs):
    return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, pos, last_plant, memo):
    key = (pos, last_plant)
    if key in memo:
        return memo[key]

    # base cases
    if pos == len(costs):
        return 0

    min_cost = float('inf')

    # Enumerate to get plant_type (index), plant_cost (value)
    for plant, cost in enumerate(costs[pos]):
        if plant != last_plant:
            candidate = cost + _positioning_plants(costs, pos + 1, plant, memo)
            min_cost = min(candidate, min_cost)

    memo[key] = min_cost
    return min_cost

print(positioning_plants([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
])) # -> 7, by doing 4 + 1 + 2.