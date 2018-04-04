import threading
import time
import queue
from time import gmtime, strftime
class World(object):
    @staticmethod
    def world_gen():
        Peking = City(u"北平",1,[20,7], 5895, 2543,u"中華人民共和國",[],1722000)
        Nanjing = City(u"南京",2,[11,8,12,18], 5938, 2708,u"中華民國",[],1114000)
        Hankou = City(u"漢口",3,[13,14,11,10], 5848, 2740,u"中華民國",[],20976000)
        Chungchin = City(u"重慶",4,[19,21,13,9], 5746, 2747,u"中華民國",[],986000)
        Guangzhou = City(u"廣州",5,[6,17,13,14], 5836, 2877,u"中華民國",[],27210000)
        Fuzhou = City(u"福州",6,[12,14,5], 5941, 2824,u"中華民國",[],11143000)
        Tianjin = City(u"天津",7,[1,20,15], 5911, 2553,u"中華人民共和國",[],1773000)
        Shanghai = City(u"上海",8,[12,2], 5986, 2728,u"中華民國",[],4630000)
        Xian = City(u"西安",9,[16,10,19,4], 5794, 2657,u"中華人民共和國",[],628000)
        Zhengzhou = City(u"鄭州",10,[9,18,16,15,3,11], 5847, 2654,u"中華人民共和國",[],29654000)
        Hefei = City(u"合肥",11,[2,18,10,3], 5912, 2719,u"中華民國",[],22462000)
        Hangzhou = City(u"杭州",12,[2,8,6,14], 5958, 2739,u"中華民國",[],19959000)
        Changsha = City(u"長沙",13,[5,14,21,1,4], 5829, 2764,u"中華民國",[],25558000)
        Nantshang = City(u"南昌",14,[13,3,6,12,5], 5865, 2763,u"中華民國",[],12507000)
        Jinan = City(u"濟南",15,[20,7,16,10,18], 5909, 2607,u"中華人民共和國",[],38865000)
        Taiyuan = City(u"太原",16,[15,9,10,20], 5834, 2590,u"中華人民共和國",[],15247000)
        Nanning = City(u"南寧",17,[5,21], 5752, 2879,u"中華民國",[],14636000)
        Shuzhou = City(u"徐州",18,[2,0,11,15], 5916, 2657,u"中華人民共和國",[],36080000)
        Chengdou = City(u"成都",19,[9,4,21], 5696, 2727,u"中華民國",[],47437000)
        Baoding = City(u"保定",20,[1,7,16,15], 5880, 2568,u"中華人民共和國",[],28719000)
        Gueyang = City(u"貴陽",21,[19,4,13,17], 5745, 2773,u"中華民國",[],10174000)
        ROC = Nation("中華民國",[Nanjing,Hankou,Chungchin
                             ,Nantshang,Hangzhou,Changsha
                             ,Guangzhou,Fuzhou,Shanghai,Hefei
                             ,Nanning,Gueyang,Chengdou])
        PRC = Nation("中華人民共和國",[Peking,Tianjin,Xian ,Zhengzhou,Jinan,Taiyuan,Shuzhou,Baoding])
        NationList = [ROC,PRC]
        Citylist = [Nanjing,Hankou,Chungchin,Guangzhou,Fuzhou,Shanghai,Nanning,Gueyang,Nantshang,Peking,Tianjin,Shanghai,Xian ,Zhengzhou,Jinan,Taiyuan,Shuzhou,Chengdou,Baoding]
        return NationList,Citylist
class Nation:
    # diplomatic 外交1,2,3,4四位
    # 1 邦交
    # 2 傀儡（上級）
    # 3 被傀儡（下屬）
    # 4 戰爭
    def __init__(self,name,Citylist,diplomatic={}):
        self.Citylist = Citylist
        self.name = name
        self.diplomatic = diplomatic
    def calculate_man_money_add(self,man_multiply,money_multiply):
        for cities in self.Citylist:
            cities.man *= int(1+man_multiply)
            cities.money += int(cities.man * money_multiply * 0.5)
    def declar_war(self,to_nation):
        self.diplomatic = default_data.update({to_nation: 4})
    def calculate_all_man(self):
        tmp = 0
        for cities in self.Citylist:
            tmp += cities.money
        return tmp
class Army:
    # 步兵 infantry
    # 騎兵 cavalry
    # 炮兵 artillery
    def __init__(self,nation,infantry,cavalry,artillery):
        self.nation = nation
        self.infantry = infantry
        self.artillery = artillery
        elf.cavaltry = cavaltry
class City:
    def __init__(self,name,number,connect_list,pos_x,pos_y,nation,army,man,money=0):
        self.name = name
        self.number = number
        self.connect_list = connect_list
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nation = nation
        self.army = army
        self.man = man
        self.money = money
    def list_connect(self):
        print(self.connect_list)
    def check_can_connect(self,number):
        for num in self.connect_list:
            if number == num:
                return True
            return False
#
# sig_queue:
# 伺服器訊號傳遞
# 第一個 1 = 有人死了
#-------------------------------------------------------------------------
# 類別:伺服端.
#-------------------------------------------------------------------------
class Server:
    #-------------------------------------------------------------------------
    # 函數:伺服端初始化.
    #-------------------------------------------------------------------------
    def __init__(self,month,day,year):
        self.attack_list = []
        self.attack_list.clear()
        self.time_list = [month,day,year]
        self.month = month
        self.year = year
        self.day = day
        self.pause = False
        self.server_on = True
        self.sig_queue = queue.Queue()
        self.time_queue = queue.Queue()
        self.stop_queue = queue.Queue()
        self.NationList = None
        self.Citylist = []
    #-------------------------------------------------------------------------
    # 函數:伺服器地圖生成.
    #-------------------------------------------------------------------------    
    def gen_map(self):
        self.NationList,self.Citylist = World.world_gen()    
    def server_start(self):
        if self.NationList is None:
            print("Map not exits")
        else:
            self.s_thread = threading.Thread(target=self.server_thread)
            self.s_thread.start()
    #-------------------------------------------------------------------------
    # 函數:伺服滅亡傳遞.
    #-------------------------------------------------------------------------    
    def who_died(self):
        sig_not_end = True
        return_list = []
        while sig_not_end:
            if self.sig_queue.empty():
                break
            tmp = self.sig_queue.get()
            if tmp == 1:
                tmp = self.sig_queue.get()
                return_list.append(tmp)
        return return_list
    #-------------------------------------------------------------------------
    # 函數:伺服端結束.
    #-------------------------------------------------------------------------    
    def __del__(self):
        self.server_stop()        

    #-------------------------------------------------------------------------
    # 函數:請server暫停.
    #-------------------------------------------------------------------------
    def server_pause(self):
        self.pause = not self.pause
    #-------------------------------------------------------------------------
    # 函數:請server停止.
    #-------------------------------------------------------------------------
    def server_stop(self):
        self.server_on = False
        self.s_thread.join()
    #-------------------------------------------------------------------------
    # 函數:請server回傳Citylist.
    #-------------------------------------------------------------------------
    def re_citylist(self):
        return self.Citylist
    #-------------------------------------------------------------------------
    # 函數:請server回傳year.
    #-------------------------------------------------------------------------
    def re_year(self):
        return self.year
    #-------------------------------------------------------------------------
    # 函數:請server回傳month.
    #-------------------------------------------------------------------------
    def re_month(self):
        return self.month
    #-------------------------------------------------------------------------
    # 函數:請server回傳day.
    #-------------------------------------------------------------------------
    def re_day(self):
        return self.day
    #-------------------------------------------------------------------------
    # 函數:設定從何攻擊.
    #-------------------------------------------------------------------------
    def attack_list_set(self,attack_from,attack_to):
        self.attack_list.append([attack_from,attack_to])
    #-------------------------------------------------------------------------
    # 函數:時間由伺服器執行緒同步.
    #-------------------------------------------------------------------------
    def sync(self,time_list,NationList):
        self.month = time_list[0]
        self.day = time_list[1]
        self.year = time_list[2]
        self.NationList = NationList
    #-------------------------------------------------------------------------
    # 函數:伺服器座標判斷.
    #-------------------------------------------------------------------------    
    def chooseCity(self,x,y,backgrounf_pos_left,backgrounf_pos_top):
        for nations in self.NationList:
            for cities in nations.Citylist:
                if abs(cities.pos_x-(x-backgrounf_pos_left)) < 12 and abs(cities.pos_y-(y-backgrounf_pos_top)) < 12:
                    return nations,cities
        return False,False
    #-------------------------------------------------------------------------
    # 函數:主要計算.
    #-------------------------------------------------------------------------    
    def server_thread(self):
        server_now = True
        while server_now:            
            sthread_print_append = strftime("[%H:%M:%S UTC]", gmtime())+"[Server/Info]"
            #---------------------------------------------------------------------
            # 計算人口及金錢增加.
            #---------------------------------------------------------------------
            NationList = self.NationList
            for nations in NationList:
                nations.calculate_man_money_add(0.00025,0.05)
            #---------------------------------------------------------------------
            # 計算攻擊.
            #---------------------------------------------------------------------    
            for attack_lists in self.attack_list:                
                toN = attack_lists.pop()
                fromN = attack_lists.pop()
                for nation_tmp in NationList:                        
                    for cities_tmp in nation_tmp.Citylist:
                        if cities_tmp.number == fromN:
                            for nation_tmp2 in NationList:                        
                                for cities_tmp2 in nation_tmp2.Citylist:
                                    if cities_tmp2.number == toN:
                                        cities_tmp.nation = cities_tmp2.nation
                                        nation_tmp2.append(cities_tmp2)
                                        nation_tmp2.remove(cities_tmp2)
                                        
                                        
            self.attack_list.clear()
            #---------------------------------------------------------------------
            # 判斷勝利.
            #---------------------------------------------------------------------
            
            with self.sig_queue.mutex:
                self.sig_queue.queue.clear()
            for nations in self.NationList:
                tmp_cities_count = 0
                for cities in nations.Citylist:
                    if cities.nation == nations.name:
                        tmp_cities_count = tmp_cities_count + 1
                if tmp_cities_count == 0:
                    self.sig_queue.put(1)
                    self.sig_queue.put(nations.name)
                print(sthread_print_append,nations.name,"Cities count: ",tmp_cities_count)
            #---------------------------------------------------------------------
            # 計算時間.
            #---------------------------------------------------------------------
            mtod = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            self.time_list[1] = self.time_list[1] + 1
            if (self.time_list[1]>mtod[self.time_list[0]]):
                if self.time_list[0] == 2:
                    if ((self.time_list[2]%100 != 0) or (self.time_list[2]%400 == 0)) and (self.time_list[2]%4 == 0):
                        if self.time_list[1] == 30:
                            self.time_list[1] %= 29
                            self.time_list[0] += 1
                        elif self.time_list[1]==29:
                            pass
                    else:
                        self.time_list[1] %= 28
                        self.time_list[0] += 1
                else:
                    self.time_list[1] %= mtod[self.time_list[0]]
                    self.time_list[0]+=1
            if self.time_list[0]>12:
                self.time_list[0] %= 12
                self.time_list[2] += 1
            self.sync(self.time_list,self.NationList)
            self.stop_queue.put(True)
            while True:
                if not self.server_on:
                    print(sthread_print_append,"Server Stop")
                    time.sleep(2)
                    return False
                elif self.pause:
                    time.sleep(1)
                else:
                    time.sleep(1)
                    break
            
        
