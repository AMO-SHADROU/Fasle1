def reverse_array(arr):
    if len(arr) <= 1:
        return arr
    else:
        return reverse_array(arr[1:]) + [arr[0]]