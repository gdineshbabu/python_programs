# tuple basic operations
a=(10,20,30)
b=(40,50,60)
print(a+b)
print(a*3)
print(sum(a))
print(sum(b))
print(min(a))
print(min(b))
print(max(a))
print(max(b))
for i in a:
    print(i)
for i in b:
    print(i)
for j in range(len(a)):
    print(a[j])
for j in range(len(b)):
    print(b[j])
print(len(a))
print(len(b))
print(10 in a)
print(100 in b)
print(sum(a)==60)
print(sum(b)==60)
