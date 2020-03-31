"""Decorators supercharges our function. It simply a function that accepts a function,
wraps a function into another function and then enhances it or changes it"""


def my_decorator(func):
    def wrap_func():
        print("*************")
        func()
        print("*************")

    return wrap_func


@my_decorator
def hello():
    print("hellloooo")


@my_decorator
def bye():
    print("See you later")


def helloa():
    print("hellloooo")


hello2 = my_decorator(helloa)()

""""So function hello() is the same as helloa() irrespective of the method being used, 
although using Decorators makes it fasters"""
hello();
print("\n")
bye();
print("\n")
hello2;
