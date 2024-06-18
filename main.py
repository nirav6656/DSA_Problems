# Largest Element in an Array

# def largest( arr, n):
#     largest = 0
#     for a in range(n):
#         if arr[a] > largest:
#             largest = arr[a]
#     return largest

# time complexity is O(n)

# ----------------------------------

# Second Largest Element in an Array without sorting

# def second_largest(arr):
#     largest = arr[0]
#     second = -1
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             second = largest
#             largest = arr[i]
#         elif arr[i] < largest and arr[i] > second:
#             second = arr[i]
#     return second
#
# print(second_largest([4,5,3,6,7,3,9,2,8,2]))

# 1752. Check if Array Is Sorted and Rotated

# def check(self, nums) -> bool:
#     n = len(nums)
#     if n == 1: return True
#     count = 0
#     for i in range(1, n):
#         if nums[i - 1] > nums[i]:
#             count += 1
#     if nums[n - 1] > nums[0]:
#         count += 1
#     if count <= 1:
#         return True
#     else:
#         return False

# 26. Remove Duplicates from Sorted Array

# def removeDuplicates(self, nums: List[int]) -> int:
#     i = 0
#
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             nums[i + 1] = nums[j]
#             i += 1
#     return i + 1
#
# print(removeDuplicates([4,5,7,8,9,9,9]))

# 283. Move Zeroes

# def move_zeros(nums):
#     n =  len(nums)
#     i = -1
#
#     for j in range(n):
#         if nums[j] == 0:
#             i = j
#             break
#     for j in range(j+1,n):
#         if nums[j] != 0:
#             temp = nums[j]
#             nums[j] = nums[i]
#             nums[i] = temp
#             i+=1
#     return nums


# Searching an element in a sorted array - Binary Search

# def binary(arr,high,low,x):
#     mid = (high + low)//2
#     if x == arr[mid]:
#         return mid
#     elif x > arr[mid]:
#         return binary(arr,high,mid+1,x)
#     else:
#         return binary(arr,mid - 1,low,x)
# arr = [1,2,3,4,5,6,7,8,9]
#
# print(binary(arr,len(arr)-1,0,6))


# Union of Two Sorted Arrays

# def findUnion(arr1, arr2, n, m):
#     union = []
#     i = j = 0
#
#     while i < n and j < m:
#         if arr1[i] < arr2[j]:
#             if len(union) == 0 or union[-1] != arr1[i]:
#                 union.append(arr1[i])
#             i += 1
#         elif arr1[i] > arr2[j]:
#             if len(union) == 0 or union[-1] != arr1[i]:
#                 union.append(arr2[j])
#             j += 1
#         else:
#             if len(union) == 0 or union[-1] != arr1[i]:
#                 union.append(arr1[i])
#             i += 1
#             j += 1
#
#     while i < n:
#         if union[-1] != arr1[i]:
#             union.append(arr1[i])
#         i += 1
#
#     while j < m:
#         if union[-1] != arr1[j]:
#             union.append(arr2[j])
#         j += 1
#
#     return union


# print(findUnion([1,2,3,4,5],[1,2,3],5,3))


# 268. Missing Number

# def missingNumber(self, nums: List[int]) -> int:
#     length = len(nums)
#     total = (length * (length + 1)) / 2
#     for i in range(length):
#         total = total - nums[i]
#     return int(total)
#
# print(missingNumber([3,0,1]))

# 485. Max Consecutive Ones
def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


print(findMaxConsecutiveOnes([1, 1, 1, 1, 0, 0, 1]))
