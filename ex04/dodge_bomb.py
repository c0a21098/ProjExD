import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))  #スクリーンのSurface
    screen_rct = screen_sfc.get_rect()            #スクリーンのRect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    #Surface
    bgimg_rct = bgimg_sfc.get_rect()              #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    kkimg_sfc = pg.image.load("fig/9.png")        #こうかとんのSurface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()             #こうかとんのRect
    kkimg_rct.center =900, 400                   #こうかとんの表示位置

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)      


        for event in pg.event.get():
            if event.type == pg.QUIT:return       #×ボタンが押されたら関数から抜け出す
        

        key_states = pg.key.get_pressed()  #辞書
        if key_states[pg.K_UP] == True:         #上下左右のキーが押されたらこうかとんが移動する
            kkimg_rct.centery -=1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery +=1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx +=1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        pg.display.update()
        clock.tick(1000)











if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()