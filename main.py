#Decorators homework


# def log_function(func):
#     def wrapper():
#         print(f"Calling Function: {func.__name__}")
#         return func()
#     return wrapper
#
#
# @log_function
# def say_hello():
#     print("Hello World!")
#
# print(say_hello())






#birinchi decorator funksiya
# def square(func):
#     def wrapper():
#         value = func()
#         return value*value
#     return wrapper
#
# #ikkinchi decorator funksiya
# def sum(func):
#     def wrapper():
#         value = func()
#         return value+value
#     return wrapper
#
# @sum
# @square
# def misol_1():
#     return 3
#
# @square
# @sum
# def misol_2():
#     return 7
#
# print(misol_1())
# print(misol_2())