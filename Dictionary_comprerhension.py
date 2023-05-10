# Dictionary comprehension

a={i:i**2 for i in range(10)}
print(a)
b={ i for i in range(10)}
print(b)
c={ i for i in range(10) if i%2==0}
print(c)
d={i for i in range(10) if i%2!=0}
print(d)
a={i:i**3 for i in range(10)}
print(a)

e={'name':{'fname':'dinesh','lname':'babu'},'age':20}
print(e['name'])
print(e['name']['lname'])
