def shapeArea(n):
    steps = n-1
    i = 0
    step_list = [1]
    for i in range(steps):
        step_list.append(step_list[i] + 2)
    
    for i in range(steps):
        step_list.append(step_list[-i-2] - 2*i)

    return sum(step_list)
    

shapeArea(4)