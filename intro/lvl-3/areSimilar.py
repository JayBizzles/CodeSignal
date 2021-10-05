def areSimilar(a,b):
    miss = []
    if set(a) != set(b):
        return False
    if sorted(a) != sorted(b):
        return False

    # diffs = [num for e,num in enumerate(list(zip(a,b))) if num[0] == num[1]]
    # print(diffs)

    for e, nums in enumerate(zip(a,b)): # combines adjacent values into a set
        if nums[0] != nums[1]:
            miss.append(e)
    
    if len(miss) > 2:
        return False
    
    return True

areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279])