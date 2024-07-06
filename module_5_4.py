class Building:
    total = True
    def __init__(self, *args):
        for i in range(1, 41):
            self.args = i
            print(self.args)
h = Building()