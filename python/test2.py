class Spam:
    val = 100
    def ham(self):
        self.egg('call method')

    def egg(self,msg):
        print("{0}".format(msg))
        print(("{0}".format(self.val)))

spam = Spam()
spam.ham()


class Spam:
    def __init__(self,ham,egg):
        self.ham = ham
        self.egg = egg
    def output(self):
        sum = self.ham + self.egg
        print("{0}".format(sum))

spam = Spam(5,10)
spam.output()