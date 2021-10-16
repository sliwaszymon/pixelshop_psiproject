import random

telephone_list = []

for x in range(8):
	temp = random.randint(111111111,999999999)
	for y in range(2):
		telephone_list.append(temp)

telephone_list_set = set(telephone_list)

print(telephone_list)
print(telephone_list_set)