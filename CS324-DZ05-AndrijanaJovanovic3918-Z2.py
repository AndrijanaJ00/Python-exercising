class Osoba:
     def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

class Studnet(Osoba):
    polozen_ispit = {}
    def __init__(self, ime, prezime, broj_indeksa, smer,polozen_ispit):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa
        self.smer = smer
        self.polozen_ispit = polozen_ispit

s1 = Studnet("Nikola", "Nikolic", 3918, "IT", {"CS101": 9,"CS102": 10, "IT210": 5})
s2 = Studnet("Jana", "Peric", 3988, "IT", {"CS101": 5,"CS102": 7, "CS230": 9})

count1 = 0
count2 = 0

print("---------------------------")
if(s1.smer == s2.smer):
    print("Studneti sa brojem indeksa {} i {} su na istom smeru".format(s1.broj_indeksa, s2.broj_indeksa))
else:
    print("Studneti sa brojem indeksa {} i {} nisu na istom smeru".format(s1.broj_indeksa, s2.broj_indeksa))

print("---------------------------")
print("Student: {} {}".format(s1.ime,s1.prezime))

for i in s1.polozen_ispit:
   if(s1.polozen_ispit[i] > 5):
       print("Predmet {} je polozen, ocena: {} ".format(i, s1.polozen_ispit[i]))
       count1 = count1 + 1
   else:
       print("Predmet {} nije polozen, ocena: {} ".format(i, s1.polozen_ispit[i]))


print("Student {} {} je ukupno polozio/la {} ispita".format(s1.ime, s1.prezime, count1))

print("---------------------------------")
print("Student: {} {}".format(s2.ime,s2.prezime))
for i in s2.polozen_ispit:
   if(s2.polozen_ispit[i] > 5):
       print("Predmet {} je polozen, ocena: {} ".format(i, s2.polozen_ispit[i]))
       count2 = count2 + 1
   else:
       print("Predmet {} nije polozen, ocena: {} ".format(i, s2.polozen_ispit[i]))


print("Student {} {} je ukpno polozio/la {} ispita".format(s2.ime, s2.prezime, count2))
print("---------------------------------")

countIspiti = 0

for i in s1.polozen_ispit:
    for j in s2.polozen_ispit:
        if(i == j and s1.polozen_ispit[i] > 5 and s2.polozen_ispit[j] > 5):
            countIspiti = countIspiti + 1

if(countIspiti > 0):
    print("Studenti imaju iste ispite koje su polozili ")
else:
     print("Studenti nemaju iste ispite koje su polozili ")