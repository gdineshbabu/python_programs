# Builtin methods

a=[] # or use a=list()

# append-single argument at a time
a.append(10)
a.append(20)
a.append([30,40])
print(a)

# extend-multiple arguments at a time

a.extend([50,60,70,80])
print(a)

# insert-to insert the elements at a particle position

a.insert(7,90)
a.insert(2,25)
print(a)

# remove -to remove the element from the list
a.remove(25)
print(a)

# pop-to pop the element in the list
a.pop()

print(a)
a.pop()
print(a)

# del-delete the element at the particular position

del a[2]
print(a)

# shuffle-this can be done by using the random function by importing
import random
random.shuffle(a)
print(a)

# sort-to sort the list

a.sort()
print(a)

# to reverse the list

b=a[::-1] # the general method 
print(b)
b.reverse() # by using the rreverse method
print(b)
b.sort(reverse=True)# reverse using the boolean function 
print(b)

# count-to count the number is no.of times it could be repeated

b=a*4
print(b)
b.count(20)

# index-to find the index of the number int he list

print(a.index(20))
