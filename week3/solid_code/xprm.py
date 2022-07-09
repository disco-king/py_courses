class C:
    def c(self):
        print("C function")

class D(C):
    def c(self):
        print("D:", end=" ")
        super().c()

d = D()

d.c()