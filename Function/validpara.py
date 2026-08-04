def isValid(s):

    stack = []

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:

        if char == '(' or char == '{' or char == '[':

            stack.append(char)

        else:

            if len(stack) == 0:

                return False

            top = stack.pop()

            if mapping[char] != top:

                return False

    return len(stack) == 0


# User input
s = input("Enter brackets: ")

# Output
print(isValid(s))