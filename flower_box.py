import unittest
'''
Flower box
3, flower grow 3 unit
cannot plant flowers next to another flower
you can plant as many flowers as you want
find out what's the heighest height of flowers you can plant
'''

class Solution(unittest.TestCase):
	def maxHeight(self, box) -> int:
		cache = []

		for i in range(len(box)):
			if i < 2:
				cache.append(box[i])
			elif i == 2:
				cache.append(box[i] + box[0])
			else:
				cache.append(max(cache[i-2], cache[i-3]) + box[i])

		return max(cache[-1], cache[-2])

	def tests(self):
		self.assertEqual(self.maxHeight([3,10,3,1,2]), 12)
		self.assertEqual(self.maxHeight([3,3,3,3,1]), 7)
		self.assertEqual(self.maxHeight([3,3,3,3,3,3]), 9)
		self.assertEqual(self.maxHeight([3,3,3,3,3,4]), 10)
		self.assertEqual(self.maxHeight([9,10,9]), 18)
		self.assertEqual(self.maxHeight([10,3]), 10)


unittest.main()



# def flowerbox(nutrient_values):
# 	a = 0  # f(i - 2)
# 	b = 0  # f(i - 1)
# 	for val in nutrient_values:
# 		print(a, b)
# 		a, b = b, max(a + val, b)

# 	print(a,b)
# 	return b

# flowerbox([3,10,3,1,2])