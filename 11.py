def coin_change(n, coins, combination=[]):
    if n == 0:
        print(combination)
        return
    elif n < 0:
        return
    else:
        for i in coins:
            combination.append(i)
            coin_change(n-i, coins, combination)
            combination.pop()