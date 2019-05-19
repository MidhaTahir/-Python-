import random 
arr = []
for i in range(10):
    arr.append(random.randint(1,100))
print(arr)
minimum = min(arr)
print("The minimum number in random list is " + str(minimum)) 
minimum_position = arr.index(min(arr))
print("The minimum number position is " + str(minimum_position+1))
maximum = max(arr)
print("The maximum number in random list is " + str(maximum)) 
maximum_position = arr.index(max(arr))
print("The maximum number position is " + str(maximum_position+1))
sum = 0 
for i in range(len(arr)):
    sum = sum + arr[i]
mean = sum/len(arr)
print(mean)