def division_result(a, b):
    if a < b:
        return 0
    else:
        return 1 + division_result(a - b, b)