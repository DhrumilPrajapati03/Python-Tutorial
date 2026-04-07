# class Parent1():
#     pass

# class Parent2():
#     pass

# class child(Parent1, Parent2):
#     pass

# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")

# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")

# class Bat(Mammal, WingedAnimal):
#     pass

# # create an object of Bat class
# b1 = Bat()

# b1.mammal_info()
# b1.winged_animal_info()

class father:
    def __init__(self,car):
        self.car = car
    
    def prop(self):
        print(f"car = {self.car}")

class mother:
    def __init__(self,gold):
        self.gold = gold

    def prop(self):
        print(f"gold = {self.gold}")

class son(father,mother):

    def __init__(self,car,gold,cycle):
        father.__init__(self,car)
        mother.__init__(self,gold)
        self.cycle = cycle
        
    def prop(self):
        print(f"car = {self.car}")
        print(f"gold = {self.gold}")
        print(f"cycle = {self.cycle}")

s = son("Audi","24 karret","boss")
s.prop()