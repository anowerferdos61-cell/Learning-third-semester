# # local scope cant acces globally.
# def test():
#     x = 5
#     print(x)
# test()

# global scope can acces from everywhere . 
#  can't modifiy manually . 
# x = 100
# def test():
#     print(x)
# test()
# #  can modify by useing global key_word.
# x = 100
# def test():
#     global x
#     x = x + 10
#     print(x)
# test()
# print(x)

#  built_in scope can use everywhere.
print(len("hello"))

#  nonlocal scope  use nonlocal scope .
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
outer()


# enclosing scope . 
def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()