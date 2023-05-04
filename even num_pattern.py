#  even number right angle triangle
n=int(input("enter a number:"))
for i in range(n+1):
    for j in range(i):
        print(i*2,end=" ")
    print('')
