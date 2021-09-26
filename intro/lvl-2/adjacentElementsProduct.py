def adjacentElementsProduct(inputArray):
    i =0
    prod = []
    for i in range(len(inputArray)-1):
        num1 = inputArray[i]
        num2 = inputArray[i+1]
        prod.append(num1*num2)
    
    prod.sort(reverse = True)
    return prod[0]

adjacentElementsProduct([6,3,4,-2,-5,9])