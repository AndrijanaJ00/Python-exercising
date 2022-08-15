import random

imenik = {}
m = 3918 // 3

for i in range(m):
    imenik[i] = random.uniform(39, 18)

print(imenik.get(3918 % 3))