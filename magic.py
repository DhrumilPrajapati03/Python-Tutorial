# print(dir(int))

class String:
    
    def __init__(self, string):
        self.string = string 
        
    def __repr__(self):
        return 'Object: {}'.format(self.string)
        
    def __add__(self, other):
        return self.string + other

if __name__ == '__main__':
    
    string1 = String('Hello')
    print(string1 +' Geeks')
    print(string1.__add__("world"))
    print(string1.__repr__())
    