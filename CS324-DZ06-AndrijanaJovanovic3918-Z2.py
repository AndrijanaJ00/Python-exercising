lista = [4,5,6,2,8,3,6,2]

def srednja_vrednost(lista):
       try:
           suma = 0
           broj_elemenata = 0
           srednja_vrednost = 0
           izbacena_greska = ""  
           for tmp in lista:
                if(str(type(tmp)) == "tuple"):
                     izbacena_greska = "tuple"
                     raise TypeError
                elif(str(type(tmp)) == "str"):
                     izbacena_greska = "string"
                     raise TypeError
                elif(str(type(tmp)) == "dict"):
                     izbacena_greska = "dictionary"
                     raise TypeError
                elif(str(type(tmp)) == "list"):
                     izbacena_greska = "list"
                     raise TypeError
                else:
                   broj_elemenata =+ 1

       except TypeError:
          print("Nadjen je podatak tipa: " + izbacena_greska)


print(srednja_vrednost([1, 3, 12.2, "2","a"]))
print(srednja_vrednost([1, 3, 12.2, ["stringgg"]]))
print(srednja_vrednost([1, 3, 12.2, (12,)]))
print(srednja_vrednost([1, 3, 12.2, 12, 31, 12.123]))
