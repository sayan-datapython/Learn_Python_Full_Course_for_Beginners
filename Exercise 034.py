pay = float(input('Enter your salary: '))

if pay <= 1250:
  newpay1 = pay + (pay * 0.15)
  print('Your new salary is {:.2f}'.format(newpay1))
else:
  newpay2 = pay + (pay * 0.10)
  print('Your new salary is {:.2f}'.format(newpay2))
