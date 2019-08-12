#A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

my_dict = {
    "Name"  : "Midha",
    "Fname" : "Tahir",
    "University": "NED",
}

#Accessing dictionary 
print(my_dict["Name"])
print(my_dict.get("Fname"))

#Changing Values
my_dict["Fname"] = "Khan"
print(my_dict)

#Looping through a dictionary 
for x in my_dict:
    print(x) 

for k in my_dict.keys(): #looping through keys
    print(k)

for v in my_dict.values(): #looping through values
    print(v)

for k,v in my_dict.items(): #looping through both keys and values
    print(k + ":" + v)

#Check if key exists 
if "Fname" in my_dict:
    print(my_dict["Fname"])

#Length of dictionary
print(len(my_dict))

#Adding Item
my_dict["Star"] = "Taurus"
print(my_dict)

#Remove Item
z = my_dict.pop("Star")
print(z) #it pops the item of dictionary and returns value
print(my_dict)
del my_dict["University"] #we can also delete whole dictionary del my_dict , my_dict.clear()
print(my_dict)

this_dict = my_dict #It will give reference , and changes made in my_dict will change this_dict and vice versa
this_dict["Fname"] = "Tahir"
print(my_dict)

that_dict = my_dict.copy()
that_dict["Fname"] = "Khan" #or we can use that_dict = dict(my_dict) -->> these both will not pass reference
print(my_dict) 


