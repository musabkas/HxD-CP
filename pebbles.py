import heapq
n, k, m = map(int, input().split())
piles = list(map(int, input().split()))

heap = []
for p in piles:
    heapq.heappush(heap, p)

consec_pops = 0
cur = 0
for i in range(m):
    cur += 1
    to_add = len(heap)
    if cur == heap[0]:
        consec_pops += 1
        if consec_pops == n:
            print(i)
            for j in range(n, 0, -1):
                print(j, end=" ")
            break
        while len(heap) and cur == heap[0]:
            heapq.heappop(heap)
    else:
        consec_pops = 0
    heapq.heappush(heap, cur + to_add)
else:
    heap.sort(reverse=True)
    for p in heap:
        print(p - cur, end=" ")
