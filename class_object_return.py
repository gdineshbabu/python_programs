class D:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p1=D("Dinesh",20)
print("My name and my age is",p1)
