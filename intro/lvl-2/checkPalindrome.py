### Checks to see if the inputted string is a palindrome. Returns true if it is and false if it is not

def checkPalindrome(inputString):
    valid = True
    i = 0
    word_len = len(inputString)
    
    for i in range(word_len):
        fpoint = inputString[i]
        bpoint = inputString[-i-1]
        if fpoint != bpoint:
            valid = False

    if valid:
        return True
    else:
        return False      



checkPalindrome("aabaa")