class D:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello this is "+self.name+" iam",self.age,"years old")
p=D("Dinesh Babu",20)
p.myfunc()
