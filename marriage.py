for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    w.reverse()

    max_score = 0
    total = 0
    for i in range(n):
        max_score = max(max_score, w[i] + total - max_score)
        total += w[i]
    print(max_score)