from matplotlib import rcParams
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

niz_ocena = np.array([])
predmet_ocena = []
validni_odgovori = {"Y", "y"}
prosek = np.array([])

while(True):
    dodaj = input("Da li zelite da dodate novi ispit? ")

    if dodaj in validni_odgovori:
        naziv = input("Unesite ime predmeta: ")
        ocena = input("Unesite ocenu: ")
        if int(ocena) >= 6 & int(ocena) <= 10:
            niz_ocena = np.append(niz_ocena, int(ocena))
            prosek_ocena = np.sum(niz_ocena) / np.size(niz_ocena)
            predmet_ocena.append({"Predmet": naziv, "Ocena": ocena})
            prosek = np.append(prosek, prosek_ocena)
        else:
            print("Uneta je ocena manja od 6")
            continue
    else:
        break

data = pd.DataFrame.from_dict(predmet_ocena)

#Morala sam profesore da navedem putanju jer iz nekog razloga nije htelo drugacije
data.to_csv(r"E:\3.godina\1.semestar\2. CS324 - Skripting jezici\2. Domaci zadaci CS324 - Skripting jezici\CS324-DZ10-AndrijanaJovanovic3918\Student_izvestaj.csv", index=False, header = True)

brOcena = Counter(data["Ocena"])
brPoSifri = Counter(s[:2] for s in data["Predmet"])

print(f"Broj ocena: {brOcena}")
print(f"Broj polozenih ispita po sifri {brPoSifri}")

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ax.pie(brOcena.values(), labels=brOcena.keys(), autopct="%.1f%%", startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 2})

ax1 = fig.add_subplot(2, 2, (3, 4))
plt.plot(niz_ocena, "-", label="Ocena")
plt.plot(prosek, "-", label="Prosek")
plt.grid()
plt.legend()

ax2 = fig.add_subplot(2, 2, 2)
plt.barh(list(brPoSifri.keys()), list(brPoSifri.values()))
plt.xlabel("Broj polozenih ispita")
plt.ylabel("Predmet")
plt.grid()

plt.savefig("Student_izvestaj.png")
plt.show()