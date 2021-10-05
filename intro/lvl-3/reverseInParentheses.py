"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s

"""

def reverseInParentheses(inputString):
    block = []
    for e,char in enumerate(inputString):
        if char  == "(":
            block.append(e)
        elif char == ")":
            temp = inputString[block[-1]:e+1]
            inputString = inputString[:block[-1]] + temp[::-1] + inputString[e+1:]
            del block[-1]

    result = ""
    for i in range(len(inputString)):
        if inputString[i] != ")" and inputString[i] != "(":
            result+=inputString[i]
    return result
reverseInParentheses("foo(bar)(foo)")

# def stringSlice(inputString):
#     block = []
#     for e, char in enumerate(inputString):
#         if isEven(int(char)):
#             block.append(e)
#         else:
#             temp = inputString[block[-1]:e]
#     print(temp)

# def isEven(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
# stringSlice("012345678910")