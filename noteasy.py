def min_ones(N, M, A, B):
	return 1 + N*M - (N//A)*(M//B)
T = int(input())
for _ in range(T):
	N, M, A, B = map(int, input().split())
	print(min_ones(N, M, A, B))
