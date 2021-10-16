import random
import datetime

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

dictionary = dict(student_list)
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

for key in dictionary:
    age = random.randint(19,30)
    dictionary[key] = (dictionary.get(key),age,int(year)-age,str(dictionary.get(key))+"@student.uwm.edu.pl")
print(dictionary)