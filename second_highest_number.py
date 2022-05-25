
def getSecondHighest(nums):
	high = float('-inf')
	second = float('-inf')
	
	for n in nums:
		if n > high:
			# high, second = n, high
			temp = high
			high = n
			second = temp
		else:
			second = max(n, second)
	return second


n = [4,2,5,3,5]
r = getSecondHighest(n)
print(r)