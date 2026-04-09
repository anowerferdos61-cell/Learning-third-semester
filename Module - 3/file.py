# .csv = comma separeted value
# .txt = text file

# with open("msg.txt","w") as file:
#     file.write('i love python!')

# with open("msg.txt","a") as file:
#     file.write('i love python!\n')

with open("msg.txt","r") as file:
    text = file.read()
    print (text)