class Solution:
	def printTillN(self, N):
		# code here 
		if N == 0:
			return
		self.printTillN(N - 1)
		print(N, end=" ")

# Example usage:
sol = Solution()
sol.printTillN(5)