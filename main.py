# encoding: utf-8
import threading
import os, sys, random
import pygame
import _server
from pygame.locals import *
import time
from time import gmtime, strftime
# 初始字體
initfont = '教育部標準宋體UN'
# 視窗大小
canvas_width = 1280
canvas_height = 1024
# 背景圖片
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [-5300,-2300]
    def change_loc(self, location):
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
BackGround = Background('PDFtoJPG.me-1 (1).jpg', [0,0])
#-------------------------------------------------------------------------
# 函數:印城市
#-------------------------------------------------------------------------
def printCity(city):
    global canvas
    font = pygame.font.SysFont(initfont, 12)
    showFont(city.name,city.pos_x,city.pos_y)
    font = pygame.font.SysFont(initfont, 24)
#-------------------------------------------------------------------------
# 函數:計算所有人數
#-------------------------------------------------------------------------
def CaculateMan(nation):
    global Citylist
    tmp = 0
    for cities in Citylist:
            if cities.nation == nation:
                tmp += cities.man
    return tmp
#-------------------------------------------------------------------------
# 函數:計算所有錢
#-------------------------------------------------------------------------
def CaculateMoney(nation):
    global Citylist
    tmp = 0
    for cities in Citylist:
            if cities.nation == nation:
                tmp += cities.money
    return tmp
#-------------------------------------------------------------------------
# 函數:秀字.
#-------------------------------------------------------------------------
def showFont( text, x, y,color=(255, 0, 0)):
    global canvas    
    text = font.render(text, 1, color) 
    canvas.blit( text, (x,y))
# 控制伺服器之全域變數
server_run = True
#-------------------------------------------------------------------------
# 函數:初始遊戲.
#-------------------------------------------------------------------------
def resetGame():
    # 宣告使用全域變數.
    global server,game_mode, Citylist, my_nation, cities_count,month,day,year
    day = 1
    month = 1
    year = 1947
    # 城市總數
    cities_count = 21

    server = _server.Server(month,day,year)
    server.gen_map()
    server.server_start()
    Citylist = server.re_citylist()
#-------------------------------------------------------------------------
# 函數:印出所有城市.
#-------------------------------------------------------------------------
def printAllCity():
    global Citylist,font,year,month,day,Background,server
    Citylist = server.re_citylist()
    font = pygame.font.SysFont(initfont, 12)
    for cities in Citylist:
        if cities.nation == u"中華民國":
            color = (0,0,255)
        else:
            color = (255,0,0)
        showFont('●',cities.pos_x-6+BackGround.rect.left,cities.pos_y-6+BackGround.rect.top,color)
    font = pygame.font.SysFont(initfont, 24)    
pygame.init()
pygame.display.set_caption(u"世界遊戲")
my_nation = u"中華民國"
# 建立畫布大小.
canvas = pygame.display.set_mode((canvas_width, canvas_height))
# 時脈.
clock = pygame.time.Clock()
# 設定字型-黑體.
font = pygame.font.SysFont(initfont, 24)
running = True
pause = False
c_city = False
attack_mode = False
attack_from = None
attack_to = None
lose = False
win = False
# 初始遊戲.
resetGame()
time.sleep(2)
while running:
    #---------------------------------------------------------------------    
    # 同步伺服器資料
    #---------------------------------------------------------------------    
    Citylist = server.re_citylist()
    year = server.re_year()
    month = server.re_month()
    day = server.re_day()
    for tmp_nation in server.who_died():
        if tmp_nation == u"中華民國":
            lose = True
        elif tmp_nation == u"中華人民共和國":
            win = True
    #---------------------------------------------------------------------
    # 判斷輸入.
    #---------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        if BackGround.rect.left <= -50:
            BackGround.change_loc([BackGround.rect.left + 50,BackGround.rect.top])
        else:
            pass     
    if keys[K_d]:
        if BackGround.rect.left >= -7630 + pygame.display.get_surface().get_size()[0]:
            BackGround.change_loc([BackGround.rect.left - 50,BackGround.rect.top])
        else:
            pass
    if keys[K_w]:
        if BackGround.rect.top <= -50:
            BackGround.change_loc([BackGround.rect.left,BackGround.rect.top + 50])
        else:
            pass
    if keys[K_s]:
        if BackGround.rect.top >= -5610 + pygame.display.get_surface().get_size()[1]:
            BackGround.change_loc([BackGround.rect.left,BackGround.rect.top - 50])
        else:
            pass
        
    for event in pygame.event.get():        
        # 離開遊戲.
        if event.type == pygame.QUIT:
            running = False
        # 判斷按下按鈕
        if event.type == pygame.KEYDOWN:
            # 判斷按下ESC按鈕
            if event.key == pygame.K_ESCAPE:
                pause = not pause
                time.sleep(0.1)
            if event.key == pygame.K_q:    
                if pause:
                    running = False
                    server.server_stop()
                time.sleep(0.1)
            if event.key == pygame.K_k:    
                if not pause:
                    attack_mode = not attack_mode
                time.sleep(0.1)
            if event.key == pygame.K_SPACE:
                server.server_pause()
                time.sleep(0.1)
            if event.key == pygame.K_r:
                if win or lose:
                    win, lose = [False,False]
                    resetGame()
                time.sleep(0.1)
            if event.key == pygame.K_o:
                print(BackGround.rect.left,", ",BackGround.rect.top) 
            #if event.key == pygame.K_UP:
            #    BackGround.change_loc([BackGround.rect.left,BackGround.rect.top + 50])
            #if event.key == pygame.K_DOWN:
            #    BackGround.change_loc([BackGround.rect.left,BackGround.rect.top - 50])
            #if event.key == pygame.K_LEFT:
            #    BackGround.change_loc([BackGround.rect.left + 50,BackGround.rect.top])
            #if event.key == pygame.K_RIGHT:
            #    BackGround.change_loc([BackGround.rect.left - 50,BackGround.rect.top])             
        # 判斷視窗大小改變
        if event.type==VIDEORESIZE:
            canvas=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            pygame.display.flip()
        # 判斷Mouse.
        if event.type == pygame.MOUSEMOTION:
            # 判斷選取城市
            if not pause:
                c_nation, c_city = server.chooseCity(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],BackGround.rect.left,BackGround.rect.top)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判斷攻擊對象
            if attack_mode and (not pause) and c_city != False:
                print(attack_from is not None)
                print(attack_from != c_city.number)
                print((c_city.nation != my_nation))
                print((c_city.check_can_connect(attack_from)))    
                if (attack_from is not None) and (attack_from != c_city.number) and (c_city.nation != my_nation) and (c_city.check_can_connect(attack_from)):
                    attack_to = c_city.number
                    server.attack_list_set(attack_from,attack_to)
                    attack_from = None
                    attack_to = None
                elif c_city.nation == my_nation:
                    attack_from = c_city.number
#---------------------------------------------------------------------    
    # 清除畫面.
    canvas.fill([255, 255, 255])
    canvas.blit(BackGround.image, BackGround.rect)
    if win:
        showFont(u"你勝利了，你為中華民國扳回一成", 8, 2)
        showFont(u"按  Q  離開遊戲", 8, 26)
        showFont(u"按 ESC 回到遊戲", 8, 50)
        showFont(u"按  R  重新遊戲", 8, 74)
    elif lose:
        showFont(u"你戰敗了，你讓中華民國撤退台灣", 8, 2)
        showFont(u"按  Q  離開遊戲", 8, 26)
        showFont(u"按 ESC 回到遊戲", 8, 50)
        showFont(u"按  R  重新遊戲", 8, 74)
    elif pause:
        showFont(u"按  Q  離開遊戲", 8, 2)
        showFont(u"按 ESC 回到遊戲", 8, 26)
    else:
        # 顯示所有城市
        printAllCity()
        # 顯示國家狀態
        showFont(u"日期\t"+str(year)+u"年"+str(month)+u"月"+str(day)+u"日 | 人力\t"+str(CaculateMan(my_nation)) + u" | 國庫\t"+str(CaculateMoney(my_nation)), 8, 2)
        if c_city != False:
            showFont(c_city.name, 8, 26)
            showFont(c_nation.name, 8, 50)

            # 顯示攻擊模式
        if attack_mode:           
            if attack_from is not None:
                showFont(u"攻擊模式" + str(attack_from), 8, 98)
            else:
                showFont(u"攻擊模式", 8, 74)
       
            
       
    # 更新畫面.
    pygame.display.update()
    clock.tick(60)
#---------------------------------------------------------------------
# 離開遊戲.
pygame.quit()

