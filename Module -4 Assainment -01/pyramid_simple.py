n = int(input("সংখ্যা দাও: "))

for i in range(1, n + 1):
    space = " " * (n - i)
    hash = "#" * (2 * i - 1)
    print(space + hash)
