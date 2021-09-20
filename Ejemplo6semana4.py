nb = []
sueldo = []
h = []
v = []

E = (h*5)
L = (E*4)
U = (L*v)

n = int(input("N: "))
for i in range(n):
    trabajador = input("Ingrese nombre del trabajador: ")
    nb.append(trabajador)
    s = int(input("Ingrese el sueldo: "))
    sueldo.append(s)
    hora= input("Ingrese sus horas trabajadas: ")
    h.append(hora)
    valor=input("Ingrese el valor de sus horas trabajadas: ")
    v.append(valor)


print(nb)
print(sueldo)
print(U)



