v = float(input('Enter speed of your car: '))

if v >= 80:
  p = (v - 80) * 7.00
  print('You got ticket and need pay for {:.2f}'.format(p))

else:
  print('Your is ok with speed')
