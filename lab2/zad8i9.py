from file_manager import *

# ex8 in file_manager 

source = "lab2/SS/zad8i9test.txt"

FileManager.read_file(source)

FileManager.update_file(source, 'Ala ma kota.')
FileManager.read_file(source)