lista = [
    {'Indeks': 155471, 'Imie': 'Szymon', 'Nazwisko': 'Śliwa', 'Adres': 'Tołkiny', 'Płeć': True},
    {'Indeks': 155780, 'Imie': 'Maciej', 'Nazwisko': 'Szymborski', 'Adres': 'Olsztyn Okrągła', 'Płeć': True},
    {'Indeks': 155416, 'Imie': 'Weronika', 'Nazwisko': 'Krejner', 'Adres': 'Klebark Mały', 'Płeć': False},
    {'Indeks': 155432, 'Imie': 'Anna', 'Nazwisko': 'Ged', 'Adres': 'Olsztyn Grotha', 'Płeć': False}
]

string = ""
for x in range(len(lista)):
    if lista[x]['Płeć']:
        string += 'Student o numerze indeksu {} nazywa się {} {}, a jego adres to {}. '.format(lista[x]['Indeks'], 
        lista[x]['Imie'], lista[x]['Nazwisko'], lista[x]['Adres'])
    else:
        string += 'Studentka o numerze indeksu {} nazywa się {} {}, a jej adres to {}. '.format(lista[x]['Indeks'], 
        lista[x]['Imie'], lista[x]['Nazwisko'], lista[x]['Adres'])

print(string)