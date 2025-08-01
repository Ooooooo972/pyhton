class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        p_sum = 0
        max_l = 0
        sum_i = {}
        for i in range(len(arr)):
            p_sum += arr[i]
            if p_sum == k:
                max_l = i + 1
            if (p_sum - k) in sum_i:
                length = i - sum_i[p_sum - k]
                max_l = max(max_l, length)
            if p_sum not in sum_i:
                sum_i[p_sum] = i
        return max_l