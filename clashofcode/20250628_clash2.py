'''
Calculate the maximum absolute difference between two adjacent integers in the input string.
Input
Line 1: An integer N, the number of integers in the input string.
Line 2: N space-separated integers.
Output
Output the maximum absolute difference between two adjacent integers in the input string.
Constraints
2 <= N <= 10
0 <= integers in the input string <= 100000
Example
Input

3
1 2 10

Output

8

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
arr = []
for i in input().split():
    num = int(i)
    arr.append(num)


maxDiff = 0
for i in range(len(arr)-1):
    maxDiff = max(maxDiff, abs(arr[i] - arr[i+1]))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


print(maxDiff)
