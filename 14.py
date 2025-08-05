from array import array
arr = array('i', [1, 2, 3, 4, 5])
print(arr[0])
from array import array
arr = array('i', [1, 2, 3])
arr.insert(1, 4)
print(arr)

from array import array
arr1 = array('i', [1, 2, 3])
arr2 = array('i', [4, 5])
arr1 += arr2
print(arr1)

import heapq
nums = [4, 1, 3]
heapq.heapify(nums)
print(nums[0])