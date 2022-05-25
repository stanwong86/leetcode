import math

# denomination = [1, 5, 12, 19], 16
def change_making(denominations, target):
    cache = {}

    def func(i, target):
        if (i, target) in cache:
            return cache[(i, target)]

        a = None
        val = denominations[i]
        if target == val:
            a = [val]
        elif target > val:
            a = func(i, target-val) + [val]
        
        b = None
        if i > 0:
            b = func(i-1, target)
        elif i == 0 and target == 1:
            b = [val]

        if a is None:
            optimal = b
        elif b is None:
            optimal = a
        elif len(a) <= len(b):
            optimal = a
        else:
            optimal = b

        cache[(i, target)] = optimal
        return optimal

    optimal = func(len(denominations)-1, target)
    return optimal


coins = [1, 5, 12, 19]
target = 28

if __name__ == '__main__':
    for target in range(1,30):
        print(f"change_making({coins}, {target}) = {change_making(coins, target)}")
    # print(f"change_making({coins}, {target}) = {change_making(coins, target)}") 
