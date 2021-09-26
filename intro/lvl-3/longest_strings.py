def allLongestStrings(inputArray):
    length= 0
    longest_str = list()

    for strings in inputArray:
        if length <= len(strings):
            length = len(strings)
    for strings in inputArray:
        if length == len(strings):
            print(strings)
            longest_str.append(strings)
    
    print(longest_str)


allLongestStrings(["a", 
 "abc", 
 "cbd", 
 "zzzzzz", 
 "a", 
 "abcdef", 
 "asasa", 
 "aaaaaa"])