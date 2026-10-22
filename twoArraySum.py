# Two array sum
# Sum of two element in array is equal to target value and find it index number.

def twoArraySum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1 ,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return []
            
            
result = twoArraySum([2,4,5,6,7],9)
print(result)