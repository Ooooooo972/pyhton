class Solution:
    def majorityElement(self, arr):
        #code here
        count=0
        candidate=None
        for num in arr:
         if  count==0:
              candidate=num
         count+=(1 if num==candidate else -1)
              
        if  arr.count(candidate)>len(arr)//2:
            
            return candidate
        return -1
    
print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))  
print(type(type(int)))
li = ['a', 'b', 'c', 'd']
print("".join(li))
print(chr(ord('A')))  
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))