def greet(fx):
    def mfx():
        print("Hello every one")
        fx()
        print("this will be appears after hello() function")

    return mfx


@greet
def hello():
    print("Good morning")


hello()
