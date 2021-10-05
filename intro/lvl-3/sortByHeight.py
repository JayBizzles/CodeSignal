"""Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!
"""
def sortByHeight(a):
    neg_list = list()
    c_list = list()
    d_list = list()
    for i in a:
        if i is not -1:
            d_list.append(i)

    for e,i in enumerate(a):
        if i == -1:
            neg_list.append(e)
    
    d_list.sort()
    for e,i in enumerate(a):
        if e in neg_list:
            d_list.insert(e,-1)
    return d_list
    
sortByHeight([-1,150,190,170,-1,-1,160,180])