###PROGRAM TO SEARCH IN A LIST###
tem = input("Enter the item you want to find? ")
mylist = [input() for num in range(5)]
flag = False
for x in range(len(mylist)):
    if mylist[x] == item:
        print("Item is found " + item + " at location: " + str(x+1))
        flag = True
        break
    else:
        pass
if flag == False:
    print("Item is not in the list")
