
def almostIncreasingSequence(sequence):
    i = 0
    j =0
    err=0
    derr=0
    correct_list = []
    while i < (len(sequence))-1:
        if sequence[i] < sequence[i+1]:
            correct_list.append(sequence[i])
            i+=1
            print(correct_list)
        else:
            err+=1
            i+=1
    if err < 2:
        while j<(len(correct_list))-1:
            if correct_list[j] < correct_list[j+1]:
                j+=1
            else:
                derr+=1
                j+=1
        if derr == 0:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")

# almostIncreasingSequence([40,50,60,10,20,30])

# print(10* '+')

almostIncreasingSequence([1,3,2,1])