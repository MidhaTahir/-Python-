#Using Lists as Queues 
'''It is also possible to use a list as a queue, (“first-in, first-out”); 
however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, 
doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.'''

#---->Enqueue, rear part [[],[],[],[]] <------- Dequeue , front part

from collections import deque

a = deque("dh")
for i in a:
    print(i.upper() ,end = "")

print("\n")
#APPENDING
a.append("a") #add on the right side
a.appendleft("i") #add on the left side
a.appendleft("m")
print(a)

a.append("t")
a.appendleft("a")
print(a)

#Rotate
a.rotate(1) #right rotation
print(a)
a.rotate(-1)#left rotation
print(a)

#POP
a.pop() #remove the rigthmost item
a.popleft() #remove the leftmost item
print(a)

#Search
print("h" in a)

#Extend
a.extend("tahir")
print(a)
print(list(a)) #lists down all elements of a queue
print(list(reversed(a))) #reversed the elements and lists down

#Peeking
print(a[0]) #peek at leftmost item
print(a[-1]) #peek at rightmost item







