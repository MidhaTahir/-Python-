# append() adds an element at the end of the list
# clear() removes all the elements of the list 
# copy() return the copy of the list 
# count() returns the no of elements with the specified value 
# extend() add the elements of the list( or any iterable) to the end of the current list 
# index() returns the index of the first element with the specified value
# insert() adds an element at the specified position 
# pop() removes the element at the specified position 
# remove() remove the first item with the specified value
# reverse() reserve the order of the list
planets = [["Mercury",6500,6.7,0.3],["Venus",2300,6.5,4.5],["Earth",5600,3.4,0.98],
["Mars",2300,4.5,0.6],["Jupiter",8932,3.4,0.7],["Saturn",2302,12.3,5.6],["Uranus",8903,9.8,0.5],
["Neptune",2345,6.7,8.9]]
planets.append(["Pluto",8900,5.6,0.5])
print(planets)
lst2 = planets.copy()
print(lst2)
print(planets.index(["Mars",2300,4.5,0.6]))
planets.insert(4,["Mars",2300,4.5,0.6])
planets.insert(5,["Mars",2300,4.5,0.6])
print(planets)
print(planets.count(["Mars",2300,4.5,0.6]))
print(planets.pop(5))
print(planets)
planets.remove(["Mars",2300,4.5,0.6])
print(planets)
planets.reverse()
print(planets)
print("In Ascending Order:")
planets.sort()
print(planets)
print(sorted(planets))
print("In Descending Order:")
planets.sort(reverse=True) #descending order
print(planets)
planets.clear()
print(planets)
planets.extend(lst2)
print(planets)



