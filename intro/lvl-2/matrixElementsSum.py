# add upp all the values that don't appear below a zero
def matrixElementsSum(matrix):
    total = 0
    cols_skip = set()
    matrix_len = len(matrix)
    #loop like this to get each individual list length

    for row in matrix:
        for col_id, value in enumerate(row):
            if col_id in cols_skip:
                continue
            if value == 0:
                cols_skip.add(col_id)
            else:
                total+=value
                print(total)
    print(total)
    return total
    """for list in matrix:
        list_size = len(list)
        print(list.count(0))
    """
    #print(f"this is a {matrix_len} x {list_size} matrix")
    #print(matrix[i][0])
    #from this we know that there are 3 nums that are gong to be omitted in the 3rd row
    #we also know that there is going to be 1 num  ommitted from the 2nd row


matrixElementsSum([[0,1,1,2], 
[0,5,0,0], 
[2,0,3,3]])


