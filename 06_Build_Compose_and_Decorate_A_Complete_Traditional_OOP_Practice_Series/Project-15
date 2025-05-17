class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):
    pass

# Demo
d = D()
d.show()  # Which show() gets called?

print("MRO of D:", [cls.__name__ for cls in D.__mro__])
