class Testcls():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        return self.a+self.b+self.c

    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def abc(a,b,c):
        return a+b+c



test =  Testcls(5,6,7)
sum = test.add()
print(sum)
print(test.class_method())
print(Testcls.abc(1,2,3))