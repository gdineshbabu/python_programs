#printing the  10 multiples upto 100
   
a=10
while a<=100:
    print(a)
    a+=10

# printing the  user input multiples upto ten times of input

n=int(input())
i=1
while i<=10:
    print(n*i)
    i+=1

# print the reverse of a number

n=int(input())
s=0
while n!=0:
   d=n%10
   s=s*10+d
   n=n//10
print(s)
