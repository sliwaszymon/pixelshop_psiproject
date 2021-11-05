

a_list = [2,4,6]
b_list = [1,3,5]

def foo(lista1,lista2):
	result_list = []
	result_list = lista1[0::2] + lista2[1::2]
	return result_list

print(foo(a_list,b_list))