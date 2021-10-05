# Given two strings, find the number of common characters between them.
def commonCharacterCount(s1, s2):

    list1= list()
    s1list = list(s1)
    s2list = list(s2)

    for elem in s1list:
        if elem in s2list:
            list1.append(elem)
            s2list.remove(elem)
    return len(list1)


commonCharacterCount("aabcc", "adcaa")