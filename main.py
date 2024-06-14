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




















