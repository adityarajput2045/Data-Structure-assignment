def medianOfTwoArray(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    n = len(arr)
    mid = n//2
    if mid%2 == 1:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid-1])// 2

result = medianOfTwoArray([15,20,30],[25,35,16])
print(result)