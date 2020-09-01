n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))

menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3

maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3

print("Menor e {}".format(menor))
print("Maior e {}".format(maior))





