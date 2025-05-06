'''
lambda is a small anonymous function that can take any number of arguements
we get high order functions like map , filter and reduce from lambda functions.
map takes a function and a list as input and applies the function to each element of the list.
filter takes a function and a list as input and returns a list of elements that satisfy the function.
reduce takes a function and a list as input and applies the function cumulatively to the elements of the list.
'''
add  = lambda x,y: x+y
print(add(2,3)) 

#map function

num = [1,2,2,3,4,3]
sq = list(map(lambda x: x**2, num))
print(sq)

#filter function

num = [1,2,2, 3,4,3]
even = list(filter(lambda x: x%2==0, num))
print(even)

#reduce function

from functools import reduce    
num = [1,2,2,3,4,3]
sum = reduce(lambda x,y: x+y, num)
print(sum)