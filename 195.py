
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)

# Example usage
# Example usage
sol = Solution()
print(sol.nthFibonacci(5))  # Output: 5
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if (n== 0):
            return 0
        elif(n==1):
            return 1
        return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)
            