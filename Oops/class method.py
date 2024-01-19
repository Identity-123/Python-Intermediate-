class Human:
    # constructor
    def __init__(self, name, age, hobby):
        # these are known as attribute of an object
        self.name = name
        self.age = age
        self.hobby = hobby

    # method
    def result(self):
        print(f'Hi my name {self.name}. Good Morning!!')


Rajan = Human("Rajan", 20, "Sleeping")
# we can add another attribute to the Rajan,
# but we cannot add this as an attribute of an object
Rajan.Nationality = "Nepal"
print(Rajan.Nationality)
Rajan.result()

print(f"Hi i am {Rajan.name},i am {Rajan.age} years old. I am from {Rajan.Nationality}")


