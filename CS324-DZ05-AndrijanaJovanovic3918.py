class Dokument():
    def __init__(self, ime, brojReci):
        self.ime = ime
        self.brojReci = brojReci

class Knjiga(Dokument):
    pass
    def __init__(self, ime, brojReci, autor,zanr,godinaIzdavanja):
        super().__init__(ime, brojReci)
        self.autor = autor
        self.zanr = zanr
        self.godinaIzdavanja = godinaIzdavanja        

knjiga1 = Knjiga("Knjiga1", 500, "Nikola Nikolic", "Komedija", 2019)
knjiga2 = Knjiga("Knjiga2", 242, "Stefan Jankovic", "Drama", 2018)
knjiga3 = Knjiga("Knjiga3", 300, "Marija Peric", "Akcija", 2000)
knjiga4 = Knjiga("Knjiga4", 220, "Teodora Majic", "Horor", 2005)
knjiga5 = Knjiga("Knjiga5", 530, "Sofija Teodorovic", "Romantican", 2009)
knjiga6 = Knjiga("Knjiga6", 607, "Janko Jankovic", "Komedija", 2002)
knjiga7 = Knjiga("Knjiga7", 903, "Dara Peric", "SCI", 2021)
knjiga8 = Knjiga("Knjiga8", 444, "Jana Denic", "Misterija", 2017)
knjiga9 = Knjiga("Knjiga9", 892, "Darko Savic", "Akcija", 2008)
knjiga10 = Knjiga("Knjiga10", 736, "Petar Krunic", "Horor", 2013)

imenik = {"lib001": knjiga1,"lib002": knjiga2,"lib003": knjiga3,"lib004": knjiga4,"lib005": knjiga5,"lib006": knjiga6,"lib007": knjiga7,"lib008": knjiga8,"lib009": knjiga9,"lib010": knjiga10}

for i in imenik:
    print("{}: {}, {}, {}".format(i,imenik[i].zanr, imenik[i].autor, imenik[i].ime))

