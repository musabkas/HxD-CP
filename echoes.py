t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    required_k = None
    possible = True
    
    for val in arr:
        if val != -1:
            remainder = val 
            
            if required_k is None:
                required_k = remainder
            elif remainder != required_k:
                possible = False
                break
    
    print("YES" if possible else "NO")