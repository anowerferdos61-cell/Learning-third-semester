n = int(input())
arr = list(map(int,input().split()))

arr.sort()
i = 0
keep = 0
while i<n:
    temp = arr[i]
    cnt = 0
    while i<n and arr[i] == temp:
        cnt += 1
        i += 1

    if cnt >= temp :
        keep = keep + temp

rmv = n - keep
print(rmv)