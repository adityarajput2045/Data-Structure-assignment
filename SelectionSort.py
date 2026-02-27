## SElection Sort
# Case	       |   Time
# Best Case	   |   O(n²)
# Average Case |   O(n²)
# Worst Case   |   O(n²)


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        
        # Find smallest element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))