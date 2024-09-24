import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    ca_img = pg.image.load("fig/3.png")           #コウカトン召喚
    ca_img = pg.transform.flip(ca_img,True,False)  #transform　引数１：画像　引数２：左右変更　引数３：上下変更
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%800)
        screen.blit(bg_img, [x, 0])
        screen.blit(ca_img,[300,200])
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()