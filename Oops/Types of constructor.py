# There are two types of constructor in OOPs
# 1. Default constructor
# 2. Parameterized constructor

class Language:
    def __init__(self, name, level, build, use, types):
        # Parameterized constructor initializes an object with provided values
        self.name = name
        self.level = level
        self.build = build
        self.use = use
        self.types = types
        print("This is a parameterized constructor")
        print(
            f'{self.name} is a {self.level} level programming language, created by {self.build}. '
            f'It is used in {self.use} and it is {self.types} programming language')

    def default_constructor(self):
        # Default constructor initializes object with default values
        print('\n')
        print("This is a default constructor")
        print(
            f'{self.name} is a {self.level} level programming language, created by {self.build}. '
            f'It is used in {self.use} and it is {self.types} programming language')


# Creating instances of the Language class using the parameterized constructor
python = Language("Python", "high", "Guido Van Rossum", "Machine learning, In hacking also",
                  'Both strongly typed and dynamically typed')
java = Language('Java', "high", "James Gosling", "Game development, Cloud computing", "statically-typed")

# Using the default constructor for the 'python' object
python.default_constructor()
