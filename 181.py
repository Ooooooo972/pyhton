import math
class Solution:
    def jugglerSequence(self, n):
        # code here
        result=[n]
        while n!=1:
            if n%2==0:
                n=int(math.floor(n**0.5))
                
            else:
                n= int(math.floor(n**1.5))
            result.append(n)
        return result
    
print(Solution().jugglerSequence(10))
