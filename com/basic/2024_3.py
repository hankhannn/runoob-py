class King:
    barkMsg = ''

    def __init__(self):
        print("this is the parent's init method")

    def setPower(self, msg):
        self.barkMsg = msg

    def bark(self):
        print("bark: ", self.barkMsg)


p = King()
p.setPower("I can control everything")
p.bark()


class Queen(King):
    def __init__(self):
        print("this is the child's init method")

    def setPower(self, msg):
        super().setPower(msg + " include the king")


c = Queen()
c.setPower("I can control everything")
c.bark()
