def factorial_sum(n):
    if n == 1:
        return 1
    else:
        return factorial(n) + factorial_sum(n-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)