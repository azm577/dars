from os import system
from json import dumps
system("cls")

with open('natija.txt', 'r') as file: 
    lines = file.readlines()  
    print(f"Fayl {len(lines)} qatordan iborat.")  
