#tuple is actually a collection of things and it is unchangeable. It is presented by round brackets 
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days)
print(days[1])
'''in tuples count and index are operable whereas assigning new things,add,remove 
are not possible. We can iterate through tuple, search in a tuple, del tuple, use len func'''
days.count("Sunday")
print(days)
print(days.index("Sunday"))
for x in days:
    print(x)
if "Sunday" in days:
    print("Yes! Sunday is a Holiday")
print(len(days))
#del days '''now if we use del "days" will be deleted hence it will not get printed'''
''' it is also possible to use tuple constructor to make tuple '''
fruits = tuple(("mango","banana","apple"))
print(fruits)
'''Similarly we can use list constructor or phir usmy hm list waly operations apply krskty hain'''
days = list(days)
days[0] = "Sunday"
print(days)
days.pop(0)
days.insert(0,"Monday")
print(days)
days = tuple(days)
print(days)
for day in range(0,len(days)):
    if days[day] == "Saturday":
        print("Saturday is holiay")
    else:
        print("not holiday")
    




