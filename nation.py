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
    def 
    def declar_war(self,to_nation):
        self.diplomatic = default_data.update({to_nation: 4})
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

