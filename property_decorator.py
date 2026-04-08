class Employee:
    def __init__(self, name):
        self._name = name  # Leading underscore indicates "private"

    @property
    def name(self):
        """The Getter"""
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        """The Setter with validation"""
        if not value:
            raise ValueError("Name cannot be empty")
        print(f"Setting name to {value}")
        self._name = value

# Usage
emp = Employee("Alice")
print(emp.name)     # Calls the getter: "Getting name..." -> Alice
emp.name = "Bob"    # Calls the setter: "Setting name to Bob"