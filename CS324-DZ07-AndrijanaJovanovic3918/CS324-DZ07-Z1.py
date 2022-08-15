import re

index = 3918

with open("podaci.txt","r") as f:
   text_uvoz = f.read()

sablon = re.compile(r"(?m)^[0-9]{3}\s{1}.*")
result = sablon.finditer(text_uvoz)

with open('result.txt', 'w') as fw:
   for r in result:
      if str(index % 10) == r.group(0)[0]:
            fw.write(r.group(0) + "\n")
