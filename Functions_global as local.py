# Functions in python -global variables

# global variable can use as local variable by declare as global variable
a=100
def display():
    global a
    a=a+1
    print(a)
display()
    
