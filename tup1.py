def sequence(tup):
    # code here
    if len(tup)<2:
        raise  
    d=tup[1]-tup[0]
    
    return tup+ tuple(tup[-1]+(i+1)*d for i in range(3))


print(sequence((1, 2, 3)))