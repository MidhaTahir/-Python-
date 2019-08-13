'''A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.'''
#lambda arguments : expression

x = lambda a: a*10
print(x(3))

y = lambda a,b : a * b 
print(y(3,4))

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def my_func(n):
    return lambda a: a*n #here n is 11 and a is 2 

func = my_func(11)
print(func(2))