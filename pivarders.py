import pgzrun

gracz = Actor('player',(400,550))

def draw():
    screen.blit('background',(0,0))
    gracz.draw()

def update():
    sterowanieKlawiszami()

def sterowanieKlawiszami():
    if keyboard.left:
        gracz.x -= 5
    if keyboard.right:
        gracz.x += 5


pgzrun.go()