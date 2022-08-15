import random

print("Unesite ime: ")
ime = input()
print("Unesite broj indeksa: ")
brIndeksa = int(input())

niz1 = []

#Ovde sam stavila da range bude 10, nisam bila sigurna da li trebam da zadam broj ili da range bude uneti broj indeksa.

def funkcija1():
         for i in range(20):
             niz1.append(int(random.uniform(0, brIndeksa)))

def funkcija2():
        for i in range(20):
            niz1.append(int(random.uniform(-round(brIndeksa / 100), brIndeksa % 100)))

def sortiranje(niz):
    for i in range(0,len(niz)):
        for j in range(i + 1, len(niz)):
            if(niz[i] > niz[j]):
                temp = niz[i]
                niz[i] = niz[j]
                niz[j] = temp

if(len(ime) % 2 == 0):
    funkcija1()
    sortiranje(niz1)
    print(niz1)
else:
    funkcija2()
    sortiranje(niz1)
    print(niz1)

    