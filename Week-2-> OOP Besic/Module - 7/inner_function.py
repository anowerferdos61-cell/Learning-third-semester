# function is a first class object in python

def outer_function():
    print("This is the outer function")
    def inner_function():
        print("This is the inner function")
        return "Inner function result"
    return inner_function

# print(outer_function())
# print(outer_function()())

def do_something(work):
    print("Doing ")
    work()
    print("Done")

# print(do_something("coding"))

def sleeping():
    print("deaming and sleeping in python")

do_something(sleeping)