import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))  #スクリーンのSurface
    screen_rct = screen_sfc.get_rect()            #スクリーンのRect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    #Surface
    bgimg_rct = bgimg_sfc.get_rect()              #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)












if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()