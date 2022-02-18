from random import randint

class block:
    def __init__(self):
        self.bomb = False
        self.bomb_around = 0

    def __str__(self):
        if not self.bomb:
            return str(self.bomb_around)
        else:
            return "#"

w, h, c = map(int, input().split())
Pole = []

for i in range(w+1):
    a = []
    for j in range(h+1):
        a.append(block())
    Pole.append(a)
bomb_geo = []

while c > 0:
    x = randint(0, w - 1)
    y = randint(0, h - 1)
    if not Pole[x][y].bomb:
        c -= 1
        Pole[x][y].bomb = True
        Pole[x - 1][y-1].bomb_around += 1
        Pole[x - 1][y + 1].bomb_around += 1
        Pole[x - 1][y].bomb_around += 1
        Pole[x + 1][y - 1].bomb_around += 1
        Pole[x + 1][y + 1].bomb_around += 1
        Pole[x + 1][y].bomb_around += 1
        Pole[x][y - 1].bomb_around += 1
        Pole[x][y + 1].bomb_around += 1
        bomb_geo.append([x,y])
with open('output1.txt', 'w') as output:
    for i in Pole[:len(Pole)-1]:
        e = ''
        for j in i[:len(i)-1]:
            e+=str(j)
        output.writelines(e+'\n')

with open('output2.txt', 'w') as output:
    for i in bomb_geo:
        output.writelines(str(i[0]+1)+' '+ str(i[1]+1)+'\n')
