import sqlite3
import pandas as pd

con = sqlite3.connect('biiblioteka.db')
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS knjige(
                                   katBroj intager,
                                   naslov text, 
                                   izdavac text, 
                                   godinaIzdavanja intager, 
                                   izdata bool
                                    )""")


class knjiga:
    
    def __init__(self, katBroj, naslov, izdavac, godinaIzdavanja, izdata = False):
        self.katBroj = katBroj
        self.naslov = naslov
        self.izdavac = izdavac
        self.godinaIzdavanja = godinaIzdavanja
        self.izdata = izdata

    def dodajUBazu(self, connecition, cursor):
        with connecition:
            cursor.execute("INSERT INTO knjige VALUES (?, ?, ?, ?, ?)", (self.katBroj, self.naslov, self.izdavac, self.godinaIzdavanja, self.izdata))
        
        connecition.commit()

def podesiIzdat(katBroj):
    cursor.execute("UPDATE knjige SET izdata = :izdata WHERE katBroj = :katBroj", {'izdata': True,'katBroj': katBroj})

def unosSaKonzole():
    katBroj = int(input("Unesite katBroj:"))
    naslov = str(input("Unesite naslov:"))
    izdavac = str(input("Unesite izdavaca:"))
    godinaIzdavanja = int(input("Unesite godinu izdavanja:"))
    k = knjiga(katBroj, naslov, izdavac, godinaIzdavanja)
    k.dodajUBazu(con, cursor)

def prikaziSve():
    sql = pd.read_sql_query("SELECT * FROM knjige", con)
    print(sql.head())

def savremeneKnjige():
    sql = pd.read_sql('SELECT * FROM knjige WHERE godinaIzdavanja > 2000', con)
    savremene_knjige = pd.DataFrame(sql) 
    print(savremene_knjige.head())

def upisCSV():
   podaci = pd.read_sql_query("SELECT * FROM knjige", con)
   kolone_u_bazi = ["naslov", "izdavac", "godinaIzdavanja"]
   izdate_knjige = podaci[podaci.izdata == 1][kolone_u_bazi]
   izdate_knjige.to_csv(r"C:\Users\Dell\Desktop\CS324-DZ08-AndrijanaJovanovic3918\izdate_knjige.csv")

print("------------------ UNOS KNJIGE ---------------------")
unosSaKonzole()

print("------------------ SVE KNJIGE ---------------------")
prikaziSve()

print("------------------IZMENA---------------------")
podesiIzdat(1)
prikaziSve()

print("-----------------SAVREMENE KNJIGE----------------------")
savremeneKnjige()

upisCSV()

con.commit()
con.close()


