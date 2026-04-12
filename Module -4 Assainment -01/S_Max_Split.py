s = input()

c1 = 0
c2 = 0 
ans = ""
result = []
for c in s:
    if c == 'L':
        c1 += 1
        ans  += c
    elif c == "R":
        c2 += 1
        ans+=c
    if c1==c2:
        result.append(ans)
        ans = ""
        c1 = 0
        c2 = 0
    
print(len(result))
for i in result:
    print(i)