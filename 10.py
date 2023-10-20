def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return 1 / factorial(n) + recursive_sum(n - 1)
