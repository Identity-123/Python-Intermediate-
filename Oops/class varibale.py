class Human:
    # Class variables to keep track of the population and data
    population = 0  # Total number of Human instances
    data = []  # List to store names of Human instances

    def __init__(self, name, age, hobby):
        # Constructor method to initialize instance variables
        self.name = name
        self.age = age
        self.hobby = hobby

        # Increment the population count and add the name to the data list
        Human.population += 1
        Human.data.append(name)

    def result(self):
        # Method to print information about the Human instance
        print(f'Hi, I am {self.name}. I am {self.age} years old. I like to {self.hobby} in my free time.')


# Creating instances of the Human class
Rajan = Human("Rajan", 20, "Sleeping")
Samir = Human("Samir", "NA", hobby='Swimming')

# Printing the population count and names of Human instances
print(str(Human.population) + '\n' + ', '.join(Human.data))
