def setInsert(arr, n):
    #code here
    s=set(arr)
    return s
def setDisplay(s):
    #code here
    print(*sorted(s))
    
def setErase(s,x):
    #code here
    x=1
    if x in s:
        s.remove(x)
        print(f"erased {x} ")
        
    else:
        print("not found")

print("setInsert")
set1 = setInsert([1, 2, 3, 4, 5], 5)
print("setDisplay")
setDisplay(set1)
setErase(set1, 1)
print("setDisplay after erase")