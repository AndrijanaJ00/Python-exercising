import random
 
indeks = [random.randrange(1, 50, 1) for i in range(7)]

print ("Indeksi studenata u padajucem redosledu su : " +  str( sorted(indeks, reverse=True)))