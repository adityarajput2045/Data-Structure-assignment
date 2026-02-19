## Function
def twoSum(arr,target_sum):
    left = 0;
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] == target_sum:
            return (left, right)
        elif arr[left] + arr[right] < target_sum:
            left = left + 1
        else:
            right = right - 1
    return -1, -1

## Driver Code
arr = [20,60,80,90,120,240]
target_sum = 210
result = twoSum(arr, target_sum)
print(result)