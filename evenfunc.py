def even(num):
    print("Yes the number is Even! ")
    return num
def odd(num):
    print("The number is Odd")
    return num
number = int(input("Enter the number: "))
if  number%2 == 0: 
    var1 = even(number)
    print(var1)
else: 
    var2 = odd(number)
    print(var2)

