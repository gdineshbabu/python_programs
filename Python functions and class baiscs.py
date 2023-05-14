1.)

------------  # ADD ALL THE VALUES IN THE LIST - SUM IT UP  ------------

l=[]
for i in range(1,6):
    l.insert(i,i)
print("sum of the elements in the list =",sum(l))
print("The list is :",l)


 ==> output:

   sum of the elements in the list = 15
   The list is : [1, 2, 3, 4, 5]

2.)

--------- # FUNCTIONS WITH PARAMETERS  -----------

def add(a,b):
    print(a+b)
add(10,20)

==> output:

  30

---------  # FUNCTIONS WITHOUT  PARAMETER  -------------

def add():
    name=input()
    age=int(input("enter your age :"))
    print("\nMy name is:",name)
    print("My age is :",age)
add()


==> output:
   
 G.Dinesh Babu
enter your age :20

My name is: G.Dinesh Babu
My age is : 20



--------  # function with a list parameter  -----------

def list(l):
    print("The list is :",l)
    print("\nThe sum of the list elements  is :",sum(l))
l=[1,2,3,4,5]
list(l)

==> output:

The list is : [1, 2, 3, 4, 5]

The sum of the list elements  is : 15


3.)

--------------   # CLASSES AND OBJECTS  -------------


class Dinesh:    
    age = 20   
    name = "G.Dinesh Babu"    
    def display(s):    
        print("My name is :",s.name)
        print("My age is  :",s.age)
a= Dinesh()    
a.display()  

==> output:

My name is : G.Dinesh Babu
My age is  : 20


4.)

-------------  # NESTED FUNCTION-[ FUNCTION INSIDE A FUNCTION ]  -------------

def Dinesh():
    print("This is outer function")
    def hello():
        print("This is inner function")
    hello()
Dinesh()


==> output:

This is outer function
This is inner function
