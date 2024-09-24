import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2,True,False)
    ca_img = pg.image.load("fig/3.png")           #コウカトン召喚
    ca_img = pg.transform.flip(ca_img,True,False)  #transform　引数１：画像　引数２：左右変更　引数３：上下変更
    ca_rct = ca_img.get_rect()
    ca_rct.center = 300,200
    tmr = 0

    # font = pg.font.Font(None, 80)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            ca_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            ca_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            ca_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            ca_rct.move_ip((+1,0))   
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(ca_img,ca_rct)

        # txt = font.render(str(tmr), True, (255, 255, 255))
        # screen.blit(txt, [300, 100])
        # txt = font.render(str(ca_rct[1]), True, (255, 255, 255))
        # screen.blit(txt, [300, 100])
        # print(ca_rct[1])
        
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()