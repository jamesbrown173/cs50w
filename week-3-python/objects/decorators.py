def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function..")
        f()

    return wrapper


@announce
def hello():
    print("Hi!")


hello()
