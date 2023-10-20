def multiply(a, b):
    if b == 0:  # اگر b صفر باشد، ضرب برابر با صفر است
        return 0
    else:
        return a + multiply(a, b - 1)