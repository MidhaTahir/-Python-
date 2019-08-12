print("********PROGRAM TO FIND 2 LARGEST NUMBER FROM A USER-DEFINED LIST*********")
num = int(input("How many numbers you want to enter in a list? "))
my_list = [int(input("")) for x in range(num)]
max1 = my_list[0]
max2 = my_list[1]
if max1<max2:
    max1,max2 = max2,max1

for i in my_list:
    if max1<i:
        max1 = i
print("The first biggest number is: " + str(max1))
for i in my_list:
    if (max2<i) and (i != max1):
        max2 = i
print("The second biggest number is: " + str(max2))
