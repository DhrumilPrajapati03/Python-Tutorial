'''class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang=lang
        #self.name=name
        #self.id = id

rohan = Employee("Rohan Prajapati","343")
jarry = programmer("Jarry","2345","Python")
print(jarry.name)'''

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang

Rohan = programmer("Rohan Prajapati",234,"Java")
print(Rohan.name,Rohan.id,Rohan.lang)
print(Rohan.id)