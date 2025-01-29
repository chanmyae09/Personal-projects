def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

# a = add(1,2,3,4)
# print(a)

def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)

class Car:

    def __init__(self,**kw):
        self.make= kw.get("make")
        self.model = kw.get("model")
        self.color=kw.get("color")



my_car= Car(make= "Nissan")
print(my_car.model)