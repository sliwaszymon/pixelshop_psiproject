
list_of_dict = []

student_list = (
    ("Hubert Maciejewski", 132867),
    ("Konstanty Zawadzki", 173596),
    ("Kajetan Czerwiński", 155663),
    ("Edward Głowacka", 123887),
    ("Andrzej Szymczak", 187333),
    ("Patryk Kozłowski", 126654),
    ("Mariusz Sikorska", 157322),
    ("Dominik Kaźmierczak", 138866),
    ("Martin Baranowski", 122778),
    ("Roman Chmielewski", 113965),
)

numbers_list = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
)

long_string = ""

dictionary = dict(student_list)
dictionary2 = dict(numbers_list)

list_of_dict.append(dictionary)
list_of_dict.append(dictionary2)

for dictionary in list_of_dict:
	for key in dictionary:
		long_string += "klucz {} ma wartosc {} \n".format(str(dictionary[key]),str(dictionary.get(key)))
long_string = long_string.upper()
print(long_string)
