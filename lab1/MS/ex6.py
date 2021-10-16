lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_B = []

for x in range(5):
    lista_B.append(lista.pop())

lista_B.sort()

print(lista)
print(lista_B)
