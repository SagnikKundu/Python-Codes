'''
Decorators in Python are a flexible and powerful way to extend or modify the behavior of functions and methods. 
By understanding and utilizing decorators, you can write cleaner, more modular, and reusable code.
Decorators in Python are a flexible and powerful way to extend or modify the behavior of functions and methods. 
By understanding and utilizing decorators, you can write cleaner, more modular, and reusable code.
'''

''' 
def calc(x) :
    def adder(y) :
        return x+y
    return adder

calc_obj = calc(10)
answer = calc_obj(15)
print(answer)
'''
# ================================================

def hello(func) :
    def inner() :
        print('Hello')
        func()
    return inner

@hello
def greet() :
    print('John Doe') 

greet()
 
# ================================================

def decorator(func) :
    def inner(*args) :
        print('This is the inner function of the decorator')
        result = func(*args)
        print('Function executed')
        return result + 10
    return inner


def calculate(a, b) :
    print('Inside the function')
    return a + b

decorator_obj = decorator(calculate)
answer = decorator_obj(10, 5)
print(answer)

@decorator
def calculate_again(a, b) :
    print('Inside the function pt.II')
    return a + b

answer2 = calculate_again(2, 8)
print(answer2)