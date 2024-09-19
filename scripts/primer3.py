#! /usr/bin/python3
import time
from copy import copy,deepcopy


global spremenljivka
spremenljivka = 1
spr2 = True
spr3 = 0.3
spr4 = "Besedilo"
spr5 = 'besedilo'
spr6 = b'f3a'   #to je v bitih
toJeSpremenljivka7 = 7

seznam = [0.4, 0.7, 0.3] #seznam
t = (4,6,2) #tuple, ga ne moremo spreminjati
d = {"avto":"skoda", "ime":"ales", "starost":32} #dictionary

print(seznam[2])
print(t[0])
print(d["ime"])

print("seznam na mestu 2: " + str(seznam[2]))
print("seznam na mestu 2: " + repr(seznam[2]))
print(f"seznam na mestu 2: {seznam[2]}, na mestu 1 pa: {seznam[1]}")

seznam[0] = 20

d["starost"] = 33

print(d)
print(seznam)

seznam.append(88)   #doda na konec
seznam.insert(0,76) #doda na mesto nič, ostale vrednosti zamakne naprej ne izbriše...
d["naslov"] = "tržaška 25"

print(seznam)
print(d)

novseznam = seznam #to je le igranje s kazalci... ni to pravo kopiranje!
#novnovseznam = copy(seznam) #to pa dejansko prekopira vsako vrednost posebej...PROBLEM: deluje le do prvega nivoja, spiski znotraj spiskov se ne kopirajo
#novnovnovseznam = deepcopy(seznam) #to je zelo zelo potratno, res le v izrednih razmirah!!!

x, y, z = t

_, _, x1, y1, _ = seznam #nekatere vrednosti nas ne zanimajo

print(x,y,z)
print(x1,y1)







def main():
    print("je blu ze buls pa smo useenu jambral")


if __name__ == "__main__":
    main()