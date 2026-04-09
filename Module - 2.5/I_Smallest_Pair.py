T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    min_val = A[0] + A[1] + 1
    
    for i in range(N):
        for j in range(i+1, N):
            result = A[i] + A[j] + j - i
            if result < min_val:
                min_val = result
    
    print(min_val)