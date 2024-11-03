class Person:
    amount=0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.amount +=1
        
    def __str__(self):
        try:
            return "name: {}, age: {}".format(self.name,self.age)
        except:
            print("Not found")
    
    def __del__(self):
        Person.amount-=1
        print(f"{self.name} is removed")
        
if __name__ == "__main__":
    p1 = Person("Geon Peter",38)
    print(p1)
    print(p1.name)
    print(Person.amount)
    p2 = Person("Leon Peter",45)
    print(p2)
    print(Person.amount)
    del (p2)
    print(Person.amount)
    print(p2.name)