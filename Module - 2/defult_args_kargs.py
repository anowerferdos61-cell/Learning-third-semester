# def sum (*nums):
#     print(nums)
#     for num in nums:
#         print(num)

# sum (1 ,1, 2 , 3,4,5,6,7)


# def my_sum(num1, num2, *args, **kargs):
#     ans = num1 + num2
#     sumition = 0
    
#     for num in args:
#         if isinstance(num, (int, float)):
#             sumition += num
#         else:
#             print(f"Skipped non-number: {num}")

#     name = None
#     for key, value in kargs.items():
#         name = f'{key} , {value}'
    
#     return name, ans, sumition


# ans = my_sum(1, 2, 3, 4, 5, 'ferdos', 'anower', name="anower")
# print(ans)


# def show_info(**kwargs):
#     print(kwargs)

# show_info(name="anower", age=21, city="dhaka")



# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# show_info(name="anower", age=21)



def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

student_info(name="anower", dept="CSE", year=3)