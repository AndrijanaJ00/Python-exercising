import numpy as np

#1
niz1 = np.identity(3)

print(niz1)
print("---------------------------------")

#2
niz2 = np.zeros((4,4), int)
niz3 = np.full((2,2), 10)
niz2[1: -1, 1:-1] = niz3
print(niz2)
print("---------------------------------")

#3
niz4 = np.ones((5,5), int)
niz5 = np.zeros((3,3), int)
niz5[1,1] = 1

niz4[1:-1, 1: -1] = niz5

print (niz4)