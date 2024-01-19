class Info:
    """
    A class to represent personal information with default values.
    """

    # Default values for personal information
    # user define object
    name = "Rajan"
    age = 20
    hobby = "Over thinking"
    country = "Nepal"

    def info(self):
        """
        Method to print personal information in a formatted way.
        I use the "\" symbol below for better code readability.
        """
        print(f"HI, I am {self.name}. I am {self.age} years old. /"
              f"I like to do {self.hobby} in my free time. /"
              f"I was born in {self.country}.")


# Creating instances of the Info class
person1 = Info()
person2 = Info()

# Modifying information for person1
person1.name = 'Krishna'
person1.age = 21

# Modifying information for person2
person2.name = 'Kushal'
person2.age = 19
person2.hobby = "Posting stuff on social media"

# Displaying information for both persons
person1.info()
person2.info()
print("\n")
print("\n")
print(" ____This is the basic way of creating class____")
