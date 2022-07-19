import pygame as pg
import sys


class Screen:
    def __init__(self, title, wh):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.Surface((1600,900))  # Surface
        pg.draw.rect(self.bgi_sfc, (0,0,0), (0,0,1600,900)) #黒の背景のRect
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Ball:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = scr.rct.width//2
        self.rct.centery = scr.rct.height//2 
        self.vx, self.vy = vxy  # 画面の中央からスタートする

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)    


class Bar: # ボールをはじくバーのクラス
    def __init__(self, color, xy):
        self.sfc = pg.Surface((40,300)) #Surface
        self.sfc.convert()
        self.sfc.fill(color) #指定しているカラーの色にする
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen): #上と下のキーで動く
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
        self.blit(scr)

    def update2(self, scr: Screen): #ｗとｓのキーで動く
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_w]: 
            self.rct.centery -= 1
        if key_states[pg.K_s]: 
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_w]: 
                self.rct.centery += 1
            if key_states[pg.K_s]: 
                self.rct.centery -= 1
        self.blit(scr)


class Score: #点数のクラス
    def __init__(self, score1, score2):
        self.fonto = pg.font.Font(None, 100)
        self.txt = self.fonto.render(f"{score2}    {score1}", True, (255,255,255)) #黒でスコアを表示する

    def blit(self, scr: Screen):
        scr.sfc.blit(self.txt,(scr.rct.width//2-50,50)) 

    def update(self, scr: Screen):
        self.blit(scr)



def main():
    clock = pg.time.Clock()
    scr = Screen("ホッケーゲーム", (1600, 900))
    bar1 = Bar((0,255,0), (scr.rct.width-21, scr.rct.height//2))
    bar2 = Bar((0,0,255), (21, scr.rct.height//2))
    bll = Ball((255,0,0), 25, (2.5,2.5), scr)
    score1 = 0
    score2 = 0
    
    while True:
        sb = Score(score1, score2)
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if bar1.rct.colliderect(bll.rct):
            bll.vx*= -1
        if bar2.rct.colliderect(bll.rct):
            bll.vx*= -1
        if bll.rct.centerx < 25:
            score1+=1
        if bll.rct.centerx > scr.rct.width-25:
            score2+=1
        if score1>=5 and score1-score2 >=2:
            return 
        elif score2>=5 and score2-score1 >=2:
            return
        bll.update(scr)
        bar1.update(scr)
        bar2.update2(scr)
        sb.update(scr)
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()