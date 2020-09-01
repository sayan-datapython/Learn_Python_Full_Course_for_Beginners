co = float(input("CO value: "))
ca = float(input("CA value: "))
hip = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai ser {:.2f}".format(hip))

from math import hypot
co = float(input("CO value cat: "))
ca = float(input("CA value cat2: "))
hip = math.hypot(co, ca)
print("A hipotenusa e {:.2f}".format(hip))
