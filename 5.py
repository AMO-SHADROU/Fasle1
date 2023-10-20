def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], find_max(arr, n-1))