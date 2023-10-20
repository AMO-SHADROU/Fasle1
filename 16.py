def print_subsets(arr, subset=[], index=0):
    if index == len(arr):
        print(subset)
        return

    print_subsets(arr, subset, index + 1)
    print_subsets(arr, subset + [arr[index]], index + 1)