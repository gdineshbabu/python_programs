# Basic operations
a=[10,20,30]
b=[40,50,60]
print("add two lists :",a+b)
print("length(a) :",len(a))
print("length(b) :",len(b))
print("sum of elements in a list:",sum(a))
print("sum of elements in b list:",sum(b))
print("minimum element in a list :",min(a))
print("minimum element in b list :",min(b))
c=max(a)
d=max(b)
print("maximum element in a list c=",max(a))
print("maximum element in b list d=",max(b))
print("c+d=",c+d,"& max(a)+max(b)=",max(a)+max(b))
print(10 in a)
print(40 in a)
print("\na list elements:")
for i in a:
    print(i)
print("\nb list elements:")
for i in range(len(b)):
    print(b[i])
n=int(input("\nenter n value :"))
print("\nprint the elements in a for n time :",a*n)
print("\nprint the elements in b for n time :",b*n)
