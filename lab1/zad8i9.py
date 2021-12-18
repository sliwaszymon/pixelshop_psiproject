from zad10 import numery

lista_studentow = (
    (155471, "Szymon Śliwa"),
    (155780, "Maciej Szymborski"),
    (155416, "Weronika Krejner"),
    (155432, "Anna Ged"), 
)

# studenci_dict = dict(lista_studentow)

# działa tak samo ale tu łatwiej dopchnąć wartości
urodzeni = [1999, 1999, 2000, 2000]
adres = ["Tołkiny", "Olsztyn Okrągła", "Klebark Mały", "Olsztyn Grotha"]
studenci_dict = {}

for student in lista_studentow:
    studenci_dict[student[0]] = {
        "Imie i nazwisko": student[1], 
        "Numer": numery[lista_studentow.index(student)], 
        "e-mail": str(student[0])+("@student.uwm.edu.pl"),
        "Rok urodzenia" : urodzeni[lista_studentow.index(student)],
        "Adres": adres[lista_studentow.index(student)]
    }

print(studenci_dict)