def outer(a,b):

    def plus(c,d):
        return c + b

    r = plus(a,b)
    print(r)

outer(1,2)
