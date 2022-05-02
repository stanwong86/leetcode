l = []
def permutations(head, tail=''):
	if len(head) == 0:
		return tail
	
	words = []
	for i in range(len(head)):
		word = permutations(head[:i] + head[i+1:], tail + head[i])
		if type(word) == str:
			word = [word]
		words.extend(word)
	return words

w = permutations('abc')
print(w)