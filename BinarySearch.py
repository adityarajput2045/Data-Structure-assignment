## Create funtion
## Time Complexity: O(n)
## Space Complexity: O(1)
def binarySearch(arr, start, end, x):
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ## start = mid + 1
            ## or
            return binarySearch(arr, mid+1, end, x)
        else:
            ## end  = mid - 1
            ## or
            return binarySearch(arr, start, mid-1, x)
    return -1    
    

               

## Driver Code
arr = [25,32,56,65,75,89,93]
start = 0
end = len(arr) - 1
x = 65

## Function Calling 
result = binarySearch(arr, start, end, x)
print("Searching element is present at index:", result)





## Output
## Searching element is present at index: 5