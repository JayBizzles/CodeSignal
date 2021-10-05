#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

def isLucky(n):
    fhalf_int = list()
    bhalf_int = list()
    num_list = list(str(n))
    
    middle = len(num_list) // 2
    fhalf = num_list[:middle]
    bhalf = num_list[middle:]

    for i in fhalf:
        fhalf_int.append(int(i))
    
    for i in bhalf:
        bhalf_int.append(int(i))

    if sum(fhalf_int) == sum(bhalf_int):
        return True
    else:
        return False

