# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal): #inheritance happened
#     def sound(self):
#         print(self.name, "barks")

# # a = Animal("cat")
# # a.info()
# # a.sound()

# d = Dog("Tommy")
# d.info()
# d.sound()

class Father:
    def __init__(self,car):
        self.car = car

    def drive(self):
        print("this is my car")

class son(Father):
    def ride(self):
        print("this is my cycle")

a = Father("Audi")
a.drive()
# a.ride()

s = son("Audi")
s.drive()
s.ride()