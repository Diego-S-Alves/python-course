x = "cat"
def f():
    x = "bird"
    def g():
        x = "dog"
        y = "fish"
        print(x)
    g()
f()