import csv
import string

print(string.ascii_lowercase)

dani = ['pon','utor']
sati = ['1','2','3']

ugao = [1,2,3]
obim = sum(ugao)
print(obim)

with open('novi.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(dani)
    csv_writer.writerow(sati)
