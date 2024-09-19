

class student():
    def __init__(self, predmeti, ocene, letnik, napredovanje):
        self.predmeti = predmeti
        self.ocene = ocene
        self.letnik = letnik
        self.napredovanje = napredovanje

    def napredovanjeDaNE(self):
        if self.ocene[0] > 5 and self.ocene[1] > 5:
            self.napredovanje = True
        else:
            self.napredovanje = False

student1 = student(["OE1", "OE2"], [6,10], 1, None)
student2 = student(["OE1", "OE2"], [7,8], 1, None)

student1.napredovanjeDaNE()
student2.napredovanjeDaNE()

print(student1.predmeti)
print(student1.ocene)
print(student1.letnik)
print(student1.napredovanje)

print(student2.predmeti)
print(student2.ocene)
print(student2.letnik)
print(student2.napredovanje)