# what should it do if len() of lists is different?
# like for me it should take teh min of lens and then connect lists 
# to the last index of min-len but.... i dunno, this ex should me more specified

# first of all I'll take 0 as even number of index
def foo(a_list, b_list):
    c_list = []
    c_len = min(len(a_list), len(b_list))

    for x in range(c_len):
        if x%2 == 0: 
            c_list.append(b_list[x])
        else:
            c_list.append(a_list[x])
    return c_list

lista1 = [1,1,2,3,5,8,13]
lista2 = [3,6,9,12,15]
lista3 = [2,4,6,8,10,12,14]
lista4 = [17,21,25]

print(lista1, lista2, foo(lista1, lista2))
print(lista1, lista3, foo(lista1, lista3))
print(lista2, lista4, foo(lista2, lista4))
print(lista4, lista2, foo(lista4, lista2))
