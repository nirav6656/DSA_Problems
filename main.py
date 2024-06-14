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

def second_largest(arr):
    largest = arr[0]
    second = -1
    for i in range(len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second:
            second = arr[i]
    return second

print(second_largest([4,5,3,6,7,3,9,2,8,2]))