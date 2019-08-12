#strings
print("I don't want to eat")
print('He said,"Yeah I know this thing"')
print('He said,"Yeah,I don\'t know"')
print("hello\t"*5) #multiply string 5 times and prints 5 hello 

#String Manipulation:

#String Concatenation
x = 7 
y = 3
print("This is the number " + str(x))
print("This is the sum of two numbers " + str(x+y))

#Other way
x = "apples"
y = "lemons"
print("In the basket are %s and %s" %(x,y))

#Another way

fname = "John"
lname = "Son"
age = 20
print("{} {} is {} years old".format(fname,lname,age))

#Similarly
x = 7.89973
y = 38.32424
print("The x is : {0:.6} and the y is: {1:4}".format(x,y))

#using the join method 
print("".join(['I',' study',' in', ' Ned',' University']))

#String Split
print("Hello:Nick".split(":")) #it splits w.r.t to given colon(separator) and returns in a list 
print("My name is " + "Hello:Midx:World".split(":")[1]) #here we want 1st index of list after splitting

print("I am Midha".split()) #splits at space
print("I , study , in , Ned".split(", ")) #splits at ,

#max split
word = 'geeks, for, geeks, midx'
print(word.split(', ',0))
print(word.split(', ',4))
print(word.split(', ',1))
print(word.split(', ',5))
print(word.split(', ',10))



