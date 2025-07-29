import bisect

def greatestSmallerOnLeft(arr, n):
    result = []
    sorted_list = []
    
    for i in range(n):
        num = arr[i]
        idx = bisect.bisect_left(sorted_list, num)
        
        if idx > 0:
            result.append(sorted_list[idx - 1])
        else:
            result.append(-1)
        
        bisect.insort(sorted_list, num)
    
    return result
greatestSmallerOnLeft([4, 5, 2, 10, 8], 5)
print(greatestSmallerOnLeft([4, 5, 2, 10, 8], 5))
