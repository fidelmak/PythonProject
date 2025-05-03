class A:
    def b(self):
        return "Funtion inside A "
class B:
    pass
class C:
    def b(self):
        return "Funtion inside c"
class D(B, C,A):
    pass
class D(C):
    pass
d = D()

print(d.b())