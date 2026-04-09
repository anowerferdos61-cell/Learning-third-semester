A, B = map(int, input().split())
S = input()

valid = True

for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            valid = False
    else:
        if not S[i].isdigit():
            valid = False

if valid:
    print("Yes")
else:
    print("No")