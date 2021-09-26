def makeArrayConsecutive2(statues):
    statues.sort()
    i = min(statues)
    array = []


    while i < max(statues):
        array.append(i)
        i+=1

    #list comprehension :)
    #look at me go ~i~
    result = [x for x in array if x not in statues]

    return len(result)

makeArrayConsecutive2([6,2,3,8])