from datetime import date
ano = int(input('Enter a Year: '))

if ano == 0:
  ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('Bisexto')
else:
  print('Not bisexto')
