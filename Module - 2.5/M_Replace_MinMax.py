n = int(input())
arr = input().split()

a = []
for x in arr:
    a.append(int(x))

min_val = min(a)
max_val = max(a)

min_idx = a.index(min_val)
max_idx = a.index(max_val)

a[min_idx] = max_val
a[max_idx] = min_val

print(*a)