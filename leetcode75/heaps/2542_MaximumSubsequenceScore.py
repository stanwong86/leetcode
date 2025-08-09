import heapq

def maxScore(A, B, k):
    total = res = 0
    output = []
    h = []
    # sort by second element in descending order
    for a,b in sorted(zip(A, B), key=lambda x: -x[1]):
        heapq.heappush(h, a)
        total += a
        if len(h) > k:
            total -= heapq.heappop(h)
        if len(h) == k:
            output.append(total*b)
            res = max(res, total * b)
    print(output)
    return res

print(maxScore([1,3,3,2], [2,1,3,4], 3))