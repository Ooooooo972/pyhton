class Solution:
    # Helper function to calculate subset sums recursively
    def subsetSumsHelper(self, arr, index, currentSum, result):
        # Base case: If we've considered all elements, add the current sum to result
        if index == len(arr):
            result.append(currentSum)
            return

        # Include current element in subset and recurse
        self.subsetSumsHelper(arr, index + 1, currentSum + arr[index], result)

        # Exclude current element from subset and recurse
        self.subsetSumsHelper(arr, index + 1, currentSum, result)

    # Main function to return the list of subset sums
    def subsetSums(self, arr):
        result = []
        self.subsetSumsHelper(
            arr, 0, 0, result)  # Start recursion from index 0 with sum 0
        return result
    
print(Solution().subsetSums([1, 2, 3]))
