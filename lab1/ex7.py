lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_B = []

for x in range(5):
    lista_B.append(lista.pop())

lista_B.sort()

# ---------------EX6-CODE--------------------

combined = lista + lista_B
combined.insert(0,0)

combined_desc = combined.copy()
combined_desc.sort()
combined_desc.reverse()

print(combined)
print(combined_desc)