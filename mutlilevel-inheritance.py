class grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

    def Gname(self):
        print(f"my grandfather name is {self.grandfathername}")

class father(grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername = fathername
        self.grandfathername = grandfathername

    def Fname(self):
        print(f"my father name is {self.fathername}")

class son(father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname = sonname
        self.fathername = fathername
        self.grandfathername = grandfathername

    def Sname(self):
        print(f"son name is {self.sonname}")

s = son("rahul","rajesh","ramesh")
s.Sname()
s.Fname()
s.Gname()