## Using Brute Force Approach
## Time Complexiety: O(log(m*n)
def search_2d(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return f"Found at ({i}, {j})"
    return "Not Found"


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(search_2d(arr, 5))






## Using advanced approach where array is sorted
## Time Complexiety: O(log(m+n)

def search_sorted_2d(arr2, target):
    row = 0
    col = len(arr[0]) - 1

    while row < len(arr2) and col >= 0:
        if arr2[row][col] == target:
            return f"Found at ({row}, {col})"
        elif arr2[row][col] > target:
            col -= 1
        else:
            row += 1

    return "Not Found"


arr2 = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(search_sorted_2d(arr2, 5))