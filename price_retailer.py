inputs = [[1,5,20],[3,8,15],[7, 10, 8]]

def getBounds(inputs):
	start = float('inf')
	end = float('-inf')
	
	for input in inputs:
		start = min(input[0], start)
		end = max(input[1], end)
	return [start, end]

startBound, endBound = getBounds(inputs)

minPrices = [float('inf') for i in range(endBound-startBound+1)]

for start, end, price in inputs:
	for i in range(start-startBound, end-startBound+1): 
		if price < minPrices[i]:
			minPrices[i] = price


# Create arrays
outputs = []
start = 0
for i in range(len(minPrices)-1):
	if minPrices[i] != minPrices[i+1]:
		outputs.append([start+startBound, i+1+startBound, minPrices[i]])
		start = i+1
	i += 1
outputs.append([start+startBound, i+startBound, minPrices[i]])


print(outputs)