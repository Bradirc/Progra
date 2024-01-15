class A:
    def hablar(self):
        print("hola desde A")

class F:
    def hablar(self):
        print("hola desde F")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(F):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self):
        print("hola desde D")

d = D()

B.hablar(d)

