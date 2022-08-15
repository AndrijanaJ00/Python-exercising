import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

niz_ocena = np.array([])
prosek = np.array([])

fleg = True
while fleg:
  ocena = input("Uneti ocenu: ")
  if(ocena != ""):
     if(int(ocena) >= 6):     
        niz_ocena = np.append(niz_ocena, int(ocena))
        prosek_ocena = np.sum(niz_ocena) / np.size(niz_ocena)
        print(f"Prosek: {prosek_ocena}")
        prosek = np.append(prosek, prosek_ocena)
     else:
         print("Ocena je manja od 6")
  else:
    fleg = False
    break

plt.plot(niz_ocena, label='Ocene')
plt.plot(prosek, label='Prosek ocena')

plt.xlabel("Prosek")
plt.ylabel("Ocene")

plt.grid()
plt.legend()
plt.show()

ocene_pie = []
broj_ocena = []
brojanje_ocena = Counter(niz_ocena)

for ocene, broj in brojanje_ocena.items():
    ocene_pie.append(ocene)
    broj_ocena.append(broj)

plt.pie(broj_ocena, labels=ocene_pie, autopct="%.1f%%", wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Ocene")
plt.show()