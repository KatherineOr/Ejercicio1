nb = []
sueldo = []
n = int(input("N: "))
for i in range(n):
    trabajador = input("Ingrese nombre del trabajador: ")
    nb.append(trabajador)
    s = int(input("Ingrese el sueldo: "))
    sueldo.append(s)
print(nb)
print(sueldo)