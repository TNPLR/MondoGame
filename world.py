import json
class World:
              def __init__(self,name):
                            self.name = name
                            self.China = {'北平':0,'南京':1,'漢口':2,'重慶':3}
              def __init__(self,name,file):
                            self.name = name
                            self.file = file
                            self.read_json(file)
              def save_json(self):
                            f = open('world.txt','w')
                            f.write(json.dumps([self.name,self.China], sort_keys=True, indent=4, separators=(',', ': ')))              
              def read_json(self,file):
                            f = open('world.txt','r')
                            read = json.loads(f.read())
                            self.name = read.pop(0)
                            self.China = read.pop(0)
class Army:
              # 步兵 infantry
              # 騎兵 cavalry
              # 炮兵 artillery
              def __init__(self,nation,infantry,cavalry,artillery):
                            self.nation = nation
                            self.infantry = infantry
                            self.artillery = artillery
                            self.cavaltry = cavaltry
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

