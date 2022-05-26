'''
Q2. Given a forest of trees, write a function that will return the id of root of the tree having maximum number of nodes in it. 
If 2 trees have same number of nodes, then return the tree with smaller id. In any tree, each child will have single parent, 
but a parent can have multiple children. Input is given as a hashmap/dictionary, in which key is child id and value is parent-id.
For eg, INPUT: [[2,3], [5,7], [3,4], [6, 8], [1,4]]
OUTPUT: 4
Explanation: We have these trees: 2-> 3 -> 4 ; 5 ->7; 6 -> 8
1 ->4
Tree with '4' as root has maximum number of nodes i.e 4 nodes.
'''


def maxNodes(nodes):

	# 2 loops for the child to new parent mapping
	uf = []
	while nodes:
		node = nodes.pop(-1)
		child, parent = node

		i = 0
		while i < len(uf):
			if uf[i][1] == child:
				uf[i][0] = parent

			elif uf[i][0] == parent:
				parent = uf[i][1]

			i += 1

		uf.append([child, parent])

	maxId = None
	maxValue = -1
	counts = {}
	for child, parent in uf:
		if parent not in counts:
			counts[parent] = 0

		counts[parent] += 1

		if counts[parent] > maxValue:
			maxValue = counts[parent]
			maxId = parent

	return maxId

nodes = [[2,3], [5,7], [3,4], [6, 8], [1,4]]
r = maxNodes(nodes)
print(r)