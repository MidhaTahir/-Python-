from functools import reduce
# def is_even(n):
#     if n%2 == 0:
#         return n


# my_list = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(is_even,my_list)) #filter takes 2 paramters a function and a list
# print(evens) 

#instead of having a function is_even we can have a lamba fn

my_list = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda n: n%2==0 ,my_list)) #to filter out from a list
print(evens)

doubles = list(map(lambda n: n*2,evens)) #to perform func on each of the iterable obj in list
print(doubles)

sum_all = reduce(lambda a,b: a+b,doubles)
print(sum_all)


