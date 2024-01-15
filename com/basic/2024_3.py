class King:
    barkMsg = ''

    def __init__(self):
        print("this is the parent's init method")

    def setBarkMsg(self, msg):
        self.barkMsg = msg

    def bark(self):
        print("bark: ", self.barkMsg)


p = King()
p.setBarkMsg("I'm the king")
p.bark()


class Queen(King):
    def __init__(self):
        print("this is the child's init method")

    def setBarkMsg(self, msg):
        super().setBarkMsg(msg + ", I'm the queen")


c = Queen()
c.setBarkMsg("I'm the queen")
c.bark()
