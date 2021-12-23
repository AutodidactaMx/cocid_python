def outer():
    a = "local"

    def inner():
        nonlocal a
        a = "nonlocal"
        print("interna:", a)

    inner()
    print("externa:", a)

outer()
