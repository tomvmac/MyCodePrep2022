# Problem:
#
# Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.
#
# The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.
#
# You may assume that every number n is guaranteed to be an integer between 1 through 9.
#
# You may assume that the input is valid and the decompressed string will only contain alphabetic characters.


# Solution:
# 1. Iterate through the characters
# 2. Push each character into the stack, except for {
# 3. When the character is a closing brace }, pop until you see a number, then repeat the sub sequence and put it back on the stack

def decompress_braces(string):
  numbers = '123456789'
  stack = []
  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ''
        while isinstance(stack[-1], str):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)


print(decompress_braces("2{q}3{tu}v"))
# -> qqtututuv

print(decompress_braces("2{y3{o}}s"))

