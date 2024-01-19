# Decorators: - it is the function that takes another function ,updates it and then return it
def outer_function():
    message = "hi"

    def inner_function():
        print(message)

    return inner_function


my_func = outer_function()
my_func()
