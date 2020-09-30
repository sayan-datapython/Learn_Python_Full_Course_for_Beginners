n = input("Enter anything: ")
print("O tipo primitivo desde valor: ", type(n))
#print if n contain space
print("Somente espaco:", n.isspace())
#print if n contain numbers
print("E numerico:", n.isnumeric())
#print if n contain alphabets
print("E alfabetico: ", n.isalpha())
#print if n contains both numerical as well as aplhabets
print("E alfanumerico: ", n.isalnum())
#print if n is uppercase
print("E Upper: ", n.isupper())
#print if n is lowercase
print("E low: ", n.islower())
