from graphics import *
import time
import random
chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
j = 0
k = 0
l=0
m=0
ix=250
jx=ix+150
kx=jx+150
lx=kx+150
mx=lx+150
points=0

def move(b,w):
    time.sleep(0.05)
    b.move(0, 10)
    w.move(0, 10)
def destroy(i,x):
    bow=Image(Point(30,10*i),'arrows.gif')
    bow.draw(win)
    arrow = Line(Point(15, 10* i), Point(60, 10* i))
    arrow.setArrow("last")
    arrow.setFill('brown')
    arrow.setWidth(4)
    arrow.draw(win)
    time.sleep(0.4)
    for a in range(x - 60):
        arrow.move(1, 0)
    time.sleep(0.05)
    arrow.undraw()
    bow.undraw()


per='y'
while per=='y'or per=='Y':
    win = GraphWin("TYPE_CHALLENGE", 1000, 600)
    win.setBackground(color_rgb(200, 240, 100))
    ask = Text(Point(450, 330), 'ENTER NAME OF PLAYER')
    ask.draw(win)
    nam = Entry(Point(450, 352), 5)
    nam.draw(win)

    start = Text(Point(450, 370), '!!click anywhere to start!!')
    start.draw(win)
    win.getMouse()
    ask.undraw()
    nam.undraw()
    start.undraw()

    line = Line(Point(0, 530), Point(1000, 530))
    line.draw(win)
    line.setFill('black')
    line.setWidth(5)
    b = (Circle(Point(ix, 5), 30), Circle(Point(jx, 5), 30), Circle(Point(kx, 5), 30), Circle(Point(lx, 5), 30),
         Circle(Point(mx, 5), 30))
    q1 = random.choice(chars)
    w1 = Text(Point(ix, 6), q1)
    b[0].draw(win)
    b[0].setFill(color_rgb(100, 50, 200))
    b[0].setOutline('green')
    b[0].setWidth(5)
    w1.draw(win)

    q2 = random.choice(chars)
    w2 = Text(Point(jx, 6), q2)
    b[1].draw(win)
    b[1].setFill(color_rgb(200, 150, 100))
    b[1].setOutline('blue')
    b[1].setWidth(5)
    w2.draw(win)

    q3 = random.choice(chars)
    w3 = Text(Point(kx, 6), q3)
    b[2].draw(win)
    b[2].setFill(color_rgb(100, 50, 20))
    b[2].setOutline('green')
    b[2].setWidth(7)

    w3.draw(win)

    q4 = random.choice(chars)
    w4 = Text(Point(lx, 6), q4)
    b[3].draw(win)
    b[3].setFill(color_rgb(225, 200, 50))
    b[3].setOutline('blue')
    b[3].setWidth(8)

    w4.draw(win)

    q5 = random.choice(chars)
    w5 = Text(Point(mx, 6), q5)
    b[4].draw(win)
    b[4].setFill(color_rgb(135, 200, 225))
    b[4].setOutline('red')
    b[4].setWidth(5)

    w5.draw(win)
    realname = nam.getText()
    while True:
        key = win.checkKey()
        if i > 0 and i < 100:
            move(b[0], w1)
            if key == q1:
                destroy(i, ix)
                q1 = random.choice(chars)
                w1.undraw()
                w1 = Text(Point(ix, 6), q1)
                w1.draw(win)
                b[0].move(0, -10 * i)
                i = 0
                points += 1
        if (i == 50):
            break

        if k > 0 and k < 100:
            move(b[2], w3)
            if key == q3:
                destroy(k, kx)
                q3 = random.choice(chars)
                w3.undraw()
                w3 = Text(Point(kx, 6), q3)
                w3.draw(win)
                b[2].move(0, -10 * k)
                k = 0
                points += 1
        if (k == 50):
            break

        if j > 0 and j < 100:
            move(b[1], w2)
            if key == q2:
                destroy(j, jx)
                q2 = random.choice(chars)
                w2.undraw()
                w2 = Text(Point(jx, 6), q2)
                w2.draw(win)
                b[1].move(0, -10 * j)
                j = 0
                points += 1
        if (j == 50):
            break

        if m > 0 and m < 100:
            move(b[4], w5)
            if key == q5:
                destroy(m, mx)
                q5 = random.choice(chars)
                w5.undraw()
                w5 = Text(Point(mx, 6), q5)
                w5.draw(win)
                w5.setFill('pink')
                b[4].move(0, -10 * m)
                m = 0
                points += 1
        if (m == 50):
            break

        if l > 0 and l < 100:
            move(b[3], w4)
            if key == q4:
                destroy(l, lx)
                q4 = random.choice(chars)
                w4.undraw()
                w4 = Text(Point(lx, 6), q4)
                w4.draw(win)
                b[3].move(0, -10 * l)
                l = 0
                points += 1
        if (l == 50):
            break

        i += 1
        j += 1
        k += 1
        l += 1
        m += 1
    b[0].undraw()
    b[1].undraw()
    b[2].undraw()
    b[3].undraw()
    b[4].undraw()
    w1.undraw()
    w2.undraw()
    w3.undraw()
    w4.undraw()
    w5.undraw()
    line.undraw()
    gameover = Text(Point(500, 200), '!!GAME OVER!!')
    gameover.setSize(30)
    gameover.draw(win)
    time.sleep(1)
    gameover.undraw()
    nametag = Text(Point(450, 300), 'NAME:')
    nametag.draw(win)
    disName = Text(Point(500, 300), realname)
    disName.draw(win)
    scoretag = Text(Point(450, 320), 'SCORE:')
    scoretag.draw(win)
    disScore = Text(Point(490, 320), points)
    disScore.draw(win)
    permis=Text(Point(450,350),'RESTART THE GAME(y/n)')
    permis.draw(win)
    # per=win.getKey()
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    if (win.getKey() != per):
        break
    else:
        win.close()
        continue
win.close()
