import math

# denomination = [1, 5, 12, 19], 16
def change_making(denominations, target):
    cache = {}

    def func(i, target):
        if (i, target) in cache:
            return cache[(i, target)]

        a = float('inf')
        val = denominations[i]
        if target == val:
            a = 1
        elif target > val:
            a = 1 + func(i, target-val)

        b = float('inf')
        if i > 0:
            b = func(i-1, target)
        leastCoins = min(a, b)
        cache[(i, target)] = leastCoins
        return leastCoins

    
    optimal = func(len(denominations)-1, target)
    # for k, v in cache.items():
    #     print(k, v)
    return optimal


coins = [1, 5, 12, 19]
target = 28

if __name__ == '__main__':
    # for target in range(28,31):
        # print(f"change_making({coins}, {target}) = {change_making(coins, target)}")
    print(f"change_making({coins}, {target}) = {change_making(coins, target)}") 
