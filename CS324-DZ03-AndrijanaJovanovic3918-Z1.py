imenik = {"CS101": 8, "CS102": 10, "IT210": 5, "CS230": 5}

for i in imenik:
   if(imenik[i] > 5):
       print("Predmet {} je polozen, ocena: {} ".format(i, imenik[i]))
   else:
       print("Predmet {} nije polozen, ocena: {} ".format(i, imenik[i]))