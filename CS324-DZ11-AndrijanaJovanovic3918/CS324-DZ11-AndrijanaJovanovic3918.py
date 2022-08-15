import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import statistics

data = pd.read_csv(r"C:\Users\Dell\Desktop\CS324-DZ11-AndrijanaJovanovic3918\podaci.csv")
trajanje = data["Trajanje"]
program = data["NivoStudija"]
univerzitet = data["Univerzitet"]
studijsi_program = data["StudijskiProgram"]
podaci_trajanje = []
podaci_bas = []
podaci_mas = []
podaci_das = []

for broj in range(len(data)):
    podaci_trajanje.append(trajanje[broj])

print(f"Srednja vrednost trajanja studija na svim studijskim programima: {np.mean(podaci_trajanje)}")

for broj in range(len(data)):
    if "BAS" in program[broj]:
        podaci_bas.append(trajanje[broj])
    if "DAS" in program[broj]:
        podaci_das.append(trajanje[broj])
    if "MAS" in program[broj]:
        podaci_mas.append(trajanje[broj])

print(f"Srednja vrednost trajanja studija na BAS studijskom programu: {np.mean(podaci_bas)}")
print(f"Srednja vrednost trajanja studija na MAS studijskom programu: {np.mean(podaci_mas)}")
print(f"Srednja vrednost trajanja studija na DAS studijskom programu: {np.mean(podaci_das)}")

print("Najcesca vrednost trajanja studija po pojedicinacnim studijskim programima:")
d = data.groupby("StudijskiProgram")["Trajanje"].apply(statistics.mode)
for i, j in d.items():
    print(i, j)

print("Najcesca vrednost trajanja studija po univerzitetima:")
d = data.groupby("Univerzitet")["Trajanje"].apply(statistics.mode)
for i, j in d.items():
    print(i, j)

d = data["Trajanje"].to_list()
plt.hist(d)
plt.show()

d = data["Univerzitet"].to_list()
plt.hist(d)
plt.show()

brojanje = Counter(studijsi_program)
nazivi = []
broj_po_nazivu = []

for naziv, broj in brojanje.items():
    nazivi.append(naziv)
    broj_po_nazivu.append(broj)

plt.pie(broj_po_nazivu, labels=nazivi, autopct="%.1f%%", wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Po studijskom programu")
plt.show()

brojanje_po_univerzitetu = Counter(univerzitet)
univerzitet = []
broj_po_univerzitetu = []

for naziv, broj in brojanje_po_univerzitetu.items():
    univerzitet.append(naziv)
    broj_po_univerzitetu.append(broj)

plt.pie(broj_po_univerzitetu, labels=univerzitet, autopct="%.1f%%", wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Po univerzitetu")
plt.show()