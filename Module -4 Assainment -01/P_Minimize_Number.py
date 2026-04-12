n = int(input())
arr = list(map(int,input().split()))

cnt =0
while True:
    all_even = True
    for i in range(n):
        if arr[i] % 2 != 0:
            all_even = False
            break
    if all_even:
        for i in range(n):
            arr[i] = arr[i] // 2
        cnt += 1
    else:
        break
print(cnt)