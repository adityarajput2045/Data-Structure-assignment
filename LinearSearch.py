## Create funtion
## Time Complexity: O(n)
## Space Complexity: O(1)
def linearSearch(arr,x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i
    return -1        

## Driver Code
arr = [25,65,89,56,14,57,89,45,61]
x = 57

## Function Calling 
result = linearSearch(arr, x)
print("Searching element is present at index:", result)





## Output
## Searching element is present at index: 5