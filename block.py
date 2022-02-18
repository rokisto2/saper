class block:
    def __init__(self):
        self.bomb = False
        self.bomb_around = 0

    def __str__(self):
        if not self.bomb:
            return str(self.bomb_around)
        else:
            return "#"