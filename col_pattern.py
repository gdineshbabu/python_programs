#  column flow triangle numbers
n=int(input("enter a number:"))
b=0
for i in range(0,n):
    b+=1
    for j in range(i+1):
        print(j,end=" ")
    print('')
