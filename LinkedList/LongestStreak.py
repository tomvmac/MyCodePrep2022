# Problem:
#
# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.


# Solution:
# 1. Iterate list
# 2. count consecutive items, and save longest streak


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    longestStreak = 0
    currentStreak = 0
    current = head
    streakValue = None

    if current is not None:
        longestStreak = 1
        currentStreak = 1
        streakValue = current.val

    while current is not None:
        current = current.next
        if current is not None:
            if current.val == streakValue:
                currentStreak += 1
            else:
                longestStreak = max(currentStreak, longestStreak)
                currentStreak = 1
                streakValue = current.val


    longestStreak = max(currentStreak, longestStreak)

    return longestStreak


# Driver Code
a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a)) # 3