import re
string = '"I AM NOT EATING THIS " , she said. Though we know she is'
new = re.sub('[A-Z]'," ",string) #sub is substitute
print(new)
new = re.sub('[,/""]'," ",string)
print(new)
new = re.sub('[A-Z]'," ",string)
print(new)
new = re.sub('[.,\ a-z A-Z]'," ",string)
print(new)
new = re.sub('[.,\ A-Z + " "]',"",string)
print(new)

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

#################
'''findall function returns a list containing all matches, 
if no match is found an empty list returns'''
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)


#################
'''The search() function searches the string for a match, 
and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned'''
str = "The rain in Spain"
x = re.search("\s", str)
print(x)
print("The first white-space character is located in position:", x.start())

################
#split function returns a list where the string has been splited
sub = "I study in NED"
y = re.split("\s",sub)
print(y)

################
#span()
#Search for an upper case "S" character in the beginning of a word, and print its position:

str = "The rain in Spain"
x = re.search("S", str)
print(x.span())

################
#group()
#Search for an upper case "S" character in the beginning of a word, and print the word:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())

###############
#string()
#The string property returns the search string:

str = "The rain in Spain"
x = re.search("S", str)
print(x.string)



