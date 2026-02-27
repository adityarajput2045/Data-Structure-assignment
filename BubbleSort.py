## Bubble sort
## Time Complexiety:
# Worst Case	O(n²)
# Average Case	O(n²)
# Best Case (Optimized)	O(n)


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


arr = [5, 2, 9, 1, 3]
print(bubble_sort(arr))