# Palindrome Check
#
# Write a function that takes in a non-empty string and that returns a boolean representing whether
# the string is a palindrome.
#
# A palindrome is defined as a string that's written the same forward and backward. Note that
# character strings are palindromes.


def isPalindrome(string):
    palindromeFound = False

    if len(string) == 1:
        return True

    # Convert string to array of characters
    inputChars = list(string)

    # Loop
    # Compare character first character and last character
    head = 0
    tail = len(inputChars)-1
    while head != tail and head < len(inputChars)/2:
        if inputChars[head] == inputChars[tail]:
            palindromeFound = True
        else:
            palindromeFound = False

        head += 1
        tail -= 1

    return palindromeFound

# Driver code

# True
string = "abcdcba"
print(string + " should be True")
print(string + " = ", isPalindrome(string))

# False
string = "abb"
print(string + " should be False")
print(string + " = ", isPalindrome(string))

# False
string = "ab"
print(string + " should be False")
print(string + " = ", isPalindrome(string))

