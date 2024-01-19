class Human:
    # class variable
    population = 0
    data = []

    # constructor
    def __init__(self, name, age, alive=True):
        self.name = name
        self.age = age
        self.alive = alive

        # the population will increase when every new person added to Human Object
        Human.population += 1
        Human.data.append(name)

    def greet(self):
        print(f"Hey my name is {self.name}. Good morning")

    def dead(self):
        if self.alive:
            self.population -= 1
            self.alive = False
        else:
            print("this person is already dead")

    def chid(self, number):
        Human.population += number


Rajan = Human("Rajan", 20)
kushal = Human("Kushal", 19)


# Inheritance
# Human is base class
# Employee is derived class
# we can modify the bass class
# Human class is employee but employee is not a human class
class Employee(Human):
    def __init__(self, name, age, company, post):
        super().__init__(name, age)
        # attribute for Employee class
        self.company = company
        self.post = post


print(Human.population)
krishna = Employee("Krishna", 29, "Google", "Head Manager")
print(Human.population)
print(Human.data)
