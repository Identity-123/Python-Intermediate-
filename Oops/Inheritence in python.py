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
class Employee(Human):
    pass


# if we not add any data inside Employee class, then it will by default take data from Human class


e1 = Employee("Sam", 38)
print(Human.data)
