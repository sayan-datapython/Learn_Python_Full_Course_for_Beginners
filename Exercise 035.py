r1 = int(input('Enter number R1: '))
r2 = int(input('Enter number R2: '))
r3 = int(input('Enter number R3: '))

if r1 < (r2 + r3) and r2 < r1 + r3 and r3 < r1 + r2:
  print('Triangle')
else:
  print('No Triangle')
