from collections import deque
# Input
N, X = map(int, input().split())
coins = list(map(int, input().split()))
m = min(coins)
dist = [float('inf')] * m
dist[0] = 0
q = deque([0])
while q:
   r = q.popleft()
   for c in coins:
       nr = (r + c) % m
       nxt = dist[r] + c
       if nxt < dist[nr]:
           dist[nr] = nxt
           q.append(nr)
# Step 2: Compute largest impossible <= X
answer = -1
for r in range(m):
   # largest v <= X with residue r and v < dist[r]
   max_k1 = (X - r) // m
   max_k2 = (dist[r] - 1 - r) // m
   k = min(max_k1, max_k2)
   if k >= 0:
       v = r + k * m
       answer = max(answer, v)
print(answer)
