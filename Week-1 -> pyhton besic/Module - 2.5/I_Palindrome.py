string = input()
string_2 = string[::-1]
string_2 = string_2.lstrip('0')
print(string_2)
if string == string_2:
    print("YES")
else:
    print("NO")