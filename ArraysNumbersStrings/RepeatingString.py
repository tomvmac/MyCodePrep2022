# Given a string str, create a function that returns the first repeating character.
# If such character doesn't exist, return the null character '\0'.

def firstRepeatingCharacter(str):
    # your code here
    visitedLetters = {}
    strarr = list(str)
    print(strarr)
    for currStr in strarr:
        if currStr in visitedLetters:
            return currStr
        else:
            visitedLetters[currStr] = True
    return None



print(firstRepeatingCharacter("abba"))