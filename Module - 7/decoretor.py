import time
import math
def my_decorator(func):
    def inner(*args,**kwargs):
        start = time.time()
        print('time started')
        func(*args,**kwargs)
        end = time.time()
        print('time ended')
        print(f'time taken: {end-start} seconds')
    return inner

@my_decorator
def exam (n):
    print("exam time is running")
    ans = math.factorial(n)
    print(ans)

exam(5)
exam(500)