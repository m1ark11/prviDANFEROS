#! /usr/bin/python3

class clovek:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost
    
    def rojsniDan(self):
        self.starost += 1



class student(clovek):                      #class student je dobil vse lastnosti class-a clovek (dodali smo tudi v __init__)
    fakulteta = "ULFE"                      #spremenljivka, ki je skupna vsem instancam
    def __init__(self, vpSt, ime, starost):
        super().__init__(ime, starost)      #to potrebujemo da "dodamo" class clovek
        self.vpisnaSt = vpSt                #spremenljivka vezana na instanco
    
    def spremeniVpisnoSt(self,novaVpSt):
        self.vpisnaSt = novaVpSt

studentJanez = student(739, "Janez", 23)
studentMarko = student(672, "Marko", 21)

print(studentJanez.vpisnaSt)
studentJanez.vpisnaSt = 924   #za ta običajen primer bi bilo to dovolj...
studentMarko.spremeniVpisnoSt(666)  #klic funkcije, ki smo jo napisali v class-u

studentMarko.rojsniDan()
print(studentMarko.starost)


