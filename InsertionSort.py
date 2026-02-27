## Insertion Sort
## Time complexiety : 0(n)
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]      # Current element
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 2, 4, 6, 1, 3]
print(insertion_sort(arr))