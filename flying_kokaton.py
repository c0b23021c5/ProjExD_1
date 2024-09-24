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
    ca_img = pg.image.load("fig/3.png")           #コウカトン召喚 ca=キャラクター
    ca_img = pg.transform.flip(ca_img,True,False)  #transform　引数１：画像　引数２：左右変更　引数３：上下変更
    ca_rct = ca_img.get_rect()
    ca_rct.center = 300,200
    tmr = 0

    font = pg.font.Font(None, 80)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        sum_mv=[0,0]
        if key_lst[pg.K_UP]:
            sum_mv[1]=-1
        elif key_lst[pg.K_DOWN]:
            sum_mv[1]=1
        elif key_lst[pg.K_LEFT]:
            sum_mv[0]=-2
        elif key_lst[pg.K_RIGHT]:
            sum_mv[0]=2
        else:
            sum_mv[0]=-1
        ca_rct.move_ip((sum_mv[0],sum_mv[1]))   


        screen.blit(ca_img,ca_rct)

        # 動作確認
        txt = font.render(f"bg:{x}", True, (255, 255, 255))
        screen.blit(txt, [400, 0])
        x_txt = font.render(f"X:{str(ca_rct[0]+x)}", True, (255, 255, 255))
        screen.blit(x_txt, [0, 0])
        y_txt = font.render(f"Y:{str(ca_rct[1])}", True, (255, 255, 255))
        screen.blit(y_txt, [200, 0])        

        pg.display.update()
        tmr += 1
        clock.tick(400)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()