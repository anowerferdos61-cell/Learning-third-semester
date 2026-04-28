a, b = map(int, input().split())

def is_lucky (n):
    for digit in str(n):
        if digit != '4' and digit != '7':
            return False
    return True

ans = []
for num in range (a,b+1):
    if is_lucky(num):
        ans.append(num)

if ans:
    print(*ans)
else:
    print (-1)
