# Class Variabel
# Azriel Gilbert Samuel Rogito
# 1101213206
# TT4510

class Hero:

   def __init__(self,inputNama,inputHealth, inputPower,inputDefense):
       self.nama = inputNama
       self.health = inputHealth
       self.power = inputPower
       self.defense = inputDefense

hero1 = Hero("Lesley",100,300,50)
hero2 = Hero("Yu Zhong",400,80,150)
hero3 = Hero("Tigreal",1200,10,400)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
