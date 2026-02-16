def solve():
    N = int(input().strip())
    A = list(map(int, input().split()))
    A = [x - 1 for x in A]
    visited = [False] * N
    answer = 0
	for i in range(N):
		if not visited[i]:
			cur = i
            cycle_len = 0
            while not visited[cur]:
                visited[cur] = True
                cycle_len += 1
                cur = A[cur]

            answer += (cycle_len + 1) // 2; 
		print(answer)
for _ in range(int(input())):
	solve()