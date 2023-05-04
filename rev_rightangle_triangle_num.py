#  reverse right angle triangle numbers
n=int(input("enter a numbber:"))
b=0
for i in range(n,0,-1):
    b+=1
    for j in range(i):
        print(b,end=" ")
    print('')
