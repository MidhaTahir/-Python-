#Factorial Program
import math
def factbymath(n):
    return math.factorial(n)
def factorial(n):
    fact = 1
    if n==1 or 0:
        return 1
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact
def factrecursion(n):
    if n == 1 or 0:
        return 1
    else :
        return n*factrecursion(n-1)
num = int(input("Enter number whose factorial you want to find? "))
result = factorial(num)
print("The factorial of a number is: " +str(result))
result1 = factrecursion(num)
print("The factorial of a number by recursion is: " +str(result1))
result3 = factbymath(num)
print("The factorial of a number by using built in function is: " +str(result3))

