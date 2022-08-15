def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

def non_recursive(n):
    niz = []
    a = 0
    b = 1
    if n == 0 or n == 1:
        print(n)
    else:
        niz.append(a)
        niz.append(b)
        while len(niz) != n:
            temp = a + b
            niz.append(temp)
            a = b
            b = temp
    print(niz)

print("Unesite broj: ")
broj = int(input())

if broj <= 0:
   print("Broj je manje od 0")
else:
   print("Recursive Fibonacci:")
   for i in range(broj):
       print(recursive_fibonacci(i))

print("Non-Recursive: ")
non_recursive(broj)
 