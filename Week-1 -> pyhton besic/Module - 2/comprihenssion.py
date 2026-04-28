nums = [ 1,2,3,4,5,6,7,8,9,0]
odd = []
for num in nums :
    if num %2 == 1 and num %5 == 0:
        odd.append(num)
print (odd)