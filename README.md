## Autorzy: Szymon Śliwa i Maciej Szymborski
# Nazwa projektu: Pixelshop
Gotowy projekt ma zapewnić możliwość zakupu stworzonych przez nas pixelartów.
# Wstępny model bazy danych:
![Model bazy danych](/pixelshop.png?raw=true "Model bazy danych")

## Jak wystartować projekt?
# Dla programisty:
1. Pobieramy brancha
2. Tworzymy wirtualne środowisko
```py -3 -m venv .venv```
```.venv/Scripts/activate.bat```
3. Aktualizujemy pip
```python -m pip install --upgrade pip```
4. Pobieramy requirementsy dla developera
```pip install -r requirements_dev.txt```
5. Przechodzimy do folderu aplikacji
```cd pixelshop```
6. Tworzymy migracje i migrujemy je na MySQL'a
```py manage.py makemigrations```
```py manage.py migrate```
7. Tworzymy superusera
```py manage.py createsuperuser```
8. Uruchamiamy serwer :)
```py manage.py runserver```

# Dla osoby zainteresowanej:
1. Pobieramy brancha
2. Tworzymy wirtualne środowisko
```py -3 -m venv .venv```
```.venv/Scripts/activate.bat```
3. Aktualizujemy pip
```python -m pip install --upgrade pip```
4. Pobieramy requirementsy niezbędne do działania aplikacji
```pip install -r requirements.txt```
5. Uruchamiamy XAMPP Controll Panel i tworzymy bazę danych o nazwie 'pixelshop'
6. Importujemy bazę danch 'pixelshop.sql'
7. Przechodzimy do folderu aplikacji
```cd pixelshop```
8. Uruchamiamy serwer :)
```py manage.py runserver```

# Dane do kont poglądowych:
1. ```[USER / KLIENT] login:Ziomek123 hasło:StandardUser123!```
2. ```[STAFF MEMBER / PRACOWNIK] login:pracusiek3371 hasło:SuperHaslo321!```
3. ```[ADMIN / PROGRAMIST LUB OSOBA Z ABSOLUTNYM DOSTĘPEM] login:admin hasło:admin1```
