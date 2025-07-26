class Solution:
    def factorial (self, n):
        # code here
        fact=1
        for i in range(n+1):
            fact*=i
        return fact
        
print(Solution().factorial(5))  # Output: 120