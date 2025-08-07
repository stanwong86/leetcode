import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 4)
heapq.heappush(heap, 3)

print(heap)

popped = heapq.heappop(heap)
print('popped: ', popped)

print(heap)

heapq.heappush(heap, 4)


print(heap)