
class A:
    pass


class B(A):
    def test(self):
        pass
    pass


class C(B):
    pass


class D(C):
    def hahaha(self):
        B.test(self)

    pass


d = D()

print(D.__mro__)
print(C.mro())
