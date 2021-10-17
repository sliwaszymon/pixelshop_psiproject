lista1 = [x for x in range(1,11,1)]
lista2 = lista1[5:]
lista1 = lista1[:5]

print(lista1, lista2)

lista1 = lista1 + lista2
print(lista1)
lista1.insert(0, 0)
lista2 = lista1.copy()
# można po prostu wyświetlić odwrotność
# print(lista2[::-1])
# albo pierw posortować a później wyświetlić
lista2.sort(reverse=True)
print(lista2)