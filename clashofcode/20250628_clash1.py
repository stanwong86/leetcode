'''
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01
Test 1
Input
Expected output

5

0 1 1 2 3

02
Test 2
Input
Expected output

1

0

03
Test 3
Input
Expected output

2

0 1

04
Test 4
Input
Expected output

10

0 1 1 2 3 5 8 13 21 34

05
Test 5
Input
Expected output

47

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 41
'''


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())


def fib(n):
    nums = []
    if n >= 1:
        nums.append(0)
    if n >= 2:
        nums.append(1)
    
    for i in range(n-2):
        nums.append(nums[i] + nums[i+1])
    
    
    nums_s = ' '.join(str(num) for num in nums)
    return nums_s

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(fib(n))

'''
# Optional Solution
def fib(n):
    if n == 0:
        return ""

    nums = [0, 1][:n]  # Handles n = 1 and n = 2 compactly

    for _ in range(n - len(nums)):
        nums.append(nums[-1] + nums[-2])

    return ' '.join(map(str, nums))


# Input handling
n = int(input())
print(fib(n))
'''
