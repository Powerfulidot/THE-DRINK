import pygame as pg

class iONG:
    def __init__(self, surf):
        self.surf = surf
        self.surf.set_alpha(0)

    def draw(self, screen, dest):
        screen.blit(self.surf, dest)

    def update(self):
        alpha = self.surf.get_alpha() + 2
        if alpha < 255:
            self.surf.set_alpha(alpha)

pg.init()
pg.mixer.pre_init(frequency=20000)

screen = pg.display.set_mode((800, 400))
pg.display.set_caption('喝水')
clock = pg.time.Clock()

water = pg.image.load('water.jpg')
screen.blit(water, (0, 0))
drink = pg.image.load('drink.jpg')
iong = iONG(drink)

sound = pg.mixer.Sound('drink.wav')
sound.play()

while True:
    iong.draw(screen, (0, 0))
    iong.update()        

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if not pg.mixer.get_busy():
        pg.quit()
        break

    clock.tick(10)
    pg.display.update()