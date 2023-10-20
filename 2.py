def recursive_mean(arr, n):
    # شرایط پایانی
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]

    # فرض کلی: محاسبهٔ میانگینarr
    return ((n - 1) * recursive_mean(arr, n - 1) + arr[n - 1]) / n


# آرایهٔ مورد نظر
array = [4, 8, 12, 3, 9]
length = len(array)

# فراخوانی تابع بازگشتی برای محاسبهٔ میانگین
mean = recursive_mean(array, length)
print("mean is:", mean)
