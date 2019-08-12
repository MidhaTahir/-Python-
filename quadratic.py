import math
A = int(input("Enter A: ")) 
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = (B**2) - (4*A*C)
if D>0:
    print("The roots are: ")
    x1 = (-B + math.sqrt(D) ) / (2*A)
    x2 = (-B - math.sqrt(D) ) / (2*A)
    print("First Root: {0:.4} ".format(x1))
    print("Second Root: {0:.4}".format(x2))
elif D == 0:
    x = -B / 2*A
    print("The root is: {0:.4}".format(x))
else:
    print("Complex roots")
    
