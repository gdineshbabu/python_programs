# Number Triangle pattern

a=int(input())
for i in range(0,a+1):
    n=1
    for j in range(a,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print(n,end=" ")
            n+=1
    print("")
