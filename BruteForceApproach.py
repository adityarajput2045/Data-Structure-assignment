def two_sum_bruteforce(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return i, j  

    return -1 

arr = [1, 2, 3, 4, 6]
target = 6
print(two_sum_bruteforce(arr, target))
