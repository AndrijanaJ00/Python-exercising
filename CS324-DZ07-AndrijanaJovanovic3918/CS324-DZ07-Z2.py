import sqlite3

conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE predmeti(
                                    sifra_predmeta text,
                                    puno_ime_predmeta text,
                                    profesor text,
                                    godina_studiranja integer
                                    )""")


class fit_predmet:
   
    def __init__(self, sifra_predmeta, puno_ime_predmeta, profesor, godina_studiranja):
        self.sifra_predmeta = sifra_predmeta
        self.puno_ime_predmeta = puno_ime_predmeta
        self.profesor = profesor
        self.godina_studiranja = godina_studiranja

    def prikaz(self):
        return f"Sifra: {self.sifra_predmeta}\nNaziv predmeta: {self.puno_ime_predmeta}\nProfesor: {self.profesor}\nGodina studiranja: {self.godina_studiranja}\n"
    
    def dodajUBazu(self, connecition, cursor):
        with connecition:
            cursor.execute("INSERT INTO predmeti VALUES (?, ?, ?, ?)", (self.sifra_predmeta, self.puno_ime_predmeta, self.profesor, self.godina_studiranja))
        
        connecition.commit()

def prikazPoProfesoru(profesor):
    cursor.execute("SELECT * FROM predmeti WHERE profesor = :profesor", {
        "profesor": profesor
    })
    return cursor.fetchall()

predmeti = [
        fit_predmet('CS101', 'Uvod u objektno-orijentisano programiranje', 'Jovana Jovic', 1),
        fit_predmet('IT101', 'Osnove informacionih tehnologija','Goran Stamenovic', 1),
        fit_predmet('CS102', 'Objekti i apstrakcija podataka', 'Jovana Jovic', 1)
    ]


for p in predmeti:
     p.dodajUBazu(conn, cursor)

predmetPoProfesoru = prikazPoProfesoru("Jovana Jovic")
for i in predmetPoProfesoru:
    print(i)
