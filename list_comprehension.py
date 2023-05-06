# list comprehensions

# to print 0-10
a=[i for i in range(10)]
print("numbers from 0-10 :",a)

# to print even numbers in 0-10
a=[i for i in range(10) if i%2==0]
print("even mubers in the range :",a)

# to print odd numbers in 0-10
a=[i for i in range(10) if i%2!=0]
print("odd mubers in the range :",a)

# to print squares of the numbers
a=[i**2 for i in range(10)]
print("squares of the numbers from 0-10 :",a)

# to print even squares of the numbers
a=[i**2 for i in range(10) if i%2==0]
print("even squares of the numbers from 0-10 :",a)

# to print odd squares of the numbers
a=[i**2 for i in range(10) if i%2!=0]
print("odd squares of the numbers from 0-10 :",a)

# to print cubess of the numbers
a=[i**3 for i in range(10)]
print("cubes of the numbers from 0-10 :",a)

# to print even squares of the numbers
a=[i**3 for i in range(10) if i%2==0]
print("even cubes of the numbers from 0-10 :",a)

# to print odd squares of the numbers
a=[i**3 for i in range(10) if i%2!=0]
print("odd cubes of the numbers from 0-10 :",a)
