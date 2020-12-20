# クラス
class Spam:
    val = 100
    def ham(self):
        self.egg('call method')

    def egg(self,msg):
        print("{0}".format(msg))
        print(("{0}".format(self.val)))

spam = Spam()
spam.ham()

# コンストラクタ
class Spam:
    def __init__(self,ham,egg):
        self.ham = ham
        self.egg = egg
    def output(self):
        sum = self.ham + self.egg
        print("{0}".format(sum))

spam = Spam(5,10)
spam.output()

# 継承
class Base:
    basevalue = "base"
    def spam(self):
        print("Base.spam()")

    def ham(self):
        print("ham")

class Derived(Base):
    def spam(self):
        print ("Derived.spam()")
        self.ham()

derived = Derived()
print("{0}".format(derived.basevalue))
derived.ham()


# 多重継承
class A:
    def method(self):
        print("class A")

class B:
    def method(self):
        print("class B")

class C(A):
    def method(self):
        print("class C")

class D(B,C):
    pass

d = D()
d.method()